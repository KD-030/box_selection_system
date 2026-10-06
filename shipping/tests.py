from decimal import Decimal

from django.test import TestCase

from shipping.models import Box, Order, OrderItem, Product


class BoxRecommendationTests(TestCase):
    def setUp(self):
        self.small_box = Box.objects.create(
            name='Small Carton',
            internal_length_cm=30,
            internal_width_cm=20,
            internal_height_cm=10,
            max_weight_kg=5,
            cost=4.00,
        )
        self.medium_box = Box.objects.create(
            name='Medium Carton',
            internal_length_cm=50,
            internal_width_cm=30,
            internal_height_cm=20,
            max_weight_kg=10,
            cost=7.00,
        )
        self.large_box = Box.objects.create(
            name='Large Carton',
            internal_length_cm=100,
            internal_width_cm=60,
            internal_height_cm=40,
            max_weight_kg=30,
            cost=12.00,
        )

        self.laptop = Product.objects.create(
            name='Laptop',
            length_cm=18,
            width_cm=12,
            height_cm=3,
            weight_kg=1.2,
        )
        self.coffee_maker = Product.objects.create(
            name='Coffee Maker',
            length_cm=20,
            width_cm=15,
            height_cm=10,
            weight_kg=0.9,
        )
        self.library = Product.objects.create(
            name='Bookshelf',
            length_cm=90,
            width_cm=35,
            height_cm=25,
            weight_kg=20.0,
        )

    def test_recommends_cheapest_box_that_can_physically_pack_order(self):
        order = Order.objects.create(customer_name='Aisha')
        OrderItem.objects.create(order=order, product=self.laptop, quantity=2)
        OrderItem.objects.create(order=order, product=self.coffee_maker, quantity=1)

        recommended_box = order.recommend_box()

        self.assertFalse(self.small_box.can_fit_order(order))
        self.assertEqual(recommended_box, self.medium_box)

    def test_returns_none_when_no_box_can_fit(self):
        order = Order.objects.create(customer_name='Jordan')
        OrderItem.objects.create(order=order, product=self.library, quantity=2)

        self.assertIsNone(order.recommend_box())

    def test_total_weight_and_volume_are_calculated(self):
        order = Order.objects.create(customer_name='Priya')
        OrderItem.objects.create(order=order, product=self.laptop, quantity=2)
        OrderItem.objects.create(order=order, product=self.coffee_maker, quantity=1)

        self.assertEqual(order.total_weight_kg, Decimal('3.3'))
        self.assertEqual(order.total_volume_cm3, Decimal('4296.0'))

    def test_repeated_product_selections_are_combined(self):
        response = self.client.post('/', {
            'customer_name': 'Morgan',
            'product_1': self.laptop.pk,
            'quantity_1': 1,
            'product_2': self.laptop.pk,
            'quantity_2': 2,
        })

        self.assertEqual(response.status_code, 200)
        order = Order.objects.get(customer_name='Morgan')
        self.assertEqual(order.items.count(), 1)
        self.assertEqual(order.items.get(product=self.laptop).quantity, 3)

    def test_product_can_be_rotated_to_fit(self):
        rotated_box = Box.objects.create(
            name='Rotated Fit Box',
            internal_length_cm=20,
            internal_width_cm=30,
            internal_height_cm=10,
            max_weight_kg=5,
            cost=3.00,
        )
        rotated_product = Product.objects.create(
            name='Wide Product',
            length_cm=28,
            width_cm=18,
            height_cm=8,
            weight_kg=1,
        )
        order = Order.objects.create(customer_name='Taylor')
        OrderItem.objects.create(order=order, product=rotated_product, quantity=1)

        self.assertTrue(rotated_box.can_fit_order(order))

    def test_rejects_order_that_fails_three_dimensional_packing(self):
        tight_box = Box.objects.create(
            name='Cube Box',
            internal_length_cm=10,
            internal_width_cm=10,
            internal_height_cm=10,
            max_weight_kg=10,
            cost=2.00,
        )
        cube_product = Product.objects.create(
            name='Six Centimetre Cube',
            length_cm=6,
            width_cm=6,
            height_cm=6,
            weight_kg=1,
        )
        order = Order.objects.create(customer_name='Casey')
        OrderItem.objects.create(order=order, product=cube_product, quantity=2)

        self.assertLessEqual(order.total_volume_cm3, tight_box.volume_cm3())
        self.assertFalse(tight_box.can_fit_order(order))

    def test_rejects_order_over_box_weight_limit(self):
        light_box = Box.objects.create(
            name='Low Weight Limit Box',
            internal_length_cm=100,
            internal_width_cm=100,
            internal_height_cm=100,
            max_weight_kg=1,
            cost=1.00,
        )
        order = Order.objects.create(customer_name='Jamie')
        OrderItem.objects.create(order=order, product=self.laptop, quantity=1)

        self.assertFalse(light_box.can_fit_order(order))
