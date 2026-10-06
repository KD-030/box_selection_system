from decimal import Decimal
from itertools import permutations, product

from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150)
    length_cm = models.DecimalField(max_digits=6, decimal_places=2)
    width_cm = models.DecimalField(max_digits=6, decimal_places=2)
    height_cm = models.DecimalField(max_digits=6, decimal_places=2)
    weight_kg = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        ordering = ['name']

    def volume_cm3(self):
        return self.length_cm * self.width_cm * self.height_cm

    def __str__(self):
        return self.name


class Box(models.Model):
    name = models.CharField(max_length=150)
    internal_length_cm = models.DecimalField(max_digits=6, decimal_places=2)
    internal_width_cm = models.DecimalField(max_digits=6, decimal_places=2)
    internal_height_cm = models.DecimalField(max_digits=6, decimal_places=2)
    max_weight_kg = models.DecimalField(max_digits=6, decimal_places=2)
    cost = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        ordering = ['cost', 'name']

    def volume_cm3(self):
        return self.internal_length_cm * self.internal_width_cm * self.internal_height_cm

    def can_fit_order(self, order):
        order_items = list(order.items.select_related('product'))
        if not order_items:
            return False

        total_weight = sum(
            (item.product.weight_kg * item.quantity for item in order_items),
            Decimal('0'),
        )
        if total_weight > self.max_weight_kg:
            return False

        total_volume = sum(
            (item.product.volume_cm3() * item.quantity for item in order_items),
            Decimal('0'),
        )
        if total_volume > self.volume_cm3():
            return False

        dimensions = []
        for item in order_items:
            product_dimensions = (
                item.product.length_cm,
                item.product.width_cm,
                item.product.height_cm,
            )
            orientations = set(permutations(product_dimensions))
            if not any(
                length <= self.internal_length_cm
                and width <= self.internal_width_cm
                and height <= self.internal_height_cm
                for length, width, height in orientations
            ):
                return False
            dimensions.extend([product_dimensions] * item.quantity)

        return self._can_pack(dimensions)

    def _can_pack(self, item_dimensions):
        items = sorted(
            item_dimensions,
            key=lambda dimensions: (
                -dimensions[0] * dimensions[1] * dimensions[2],
                -max(dimensions),
            ),
        )
        placements = []

        for dimensions in items:
            orientations = sorted(
                set(permutations(dimensions)),
                key=lambda orientation: (-orientation[0], -orientation[1], -orientation[2]),
            )
            x_positions = {Decimal('0')}
            y_positions = {Decimal('0')}
            z_positions = {Decimal('0')}
            for x, y, z, length, width, height in placements:
                x_positions.add(x + length)
                y_positions.add(y + width)
                z_positions.add(z + height)

            positions = sorted(
                product(x_positions, y_positions, z_positions),
                key=lambda position: (position[2], position[1], position[0]),
            )
            placement = None

            for x, y, z in positions:
                for length, width, height in orientations:
                    if (
                        x + length > self.internal_length_cm
                        or y + width > self.internal_width_cm
                        or z + height > self.internal_height_cm
                    ):
                        continue

                    overlaps = any(
                        not (
                            x + length <= other_x
                            or other_x + other_length <= x
                            or y + width <= other_y
                            or other_y + other_width <= y
                            or z + height <= other_z
                            or other_z + other_height <= z
                        )
                        for (
                            other_x,
                            other_y,
                            other_z,
                            other_length,
                            other_width,
                            other_height,
                        ) in placements
                    )
                    if not overlaps:
                        placement = (x, y, z, length, width, height)
                        break
                if placement:
                    break

            if placement is None:
                return False
            placements.append(placement)

        return True

    def __str__(self):
        return f"{self.name} (${self.cost})"


class Order(models.Model):
    customer_name = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['-created_at']

    @property
    def total_weight_kg(self):
        return sum((item.product.weight_kg * item.quantity for item in self.items.all()), Decimal('0'))

    @property
    def total_volume_cm3(self):
        return sum((item.product.volume_cm3() * item.quantity for item in self.items.all()), Decimal('0'))

    def recommend_box(self):
        feasible_boxes = []
        for box in Box.objects.all():
            if box.can_fit_order(self):
                feasible_boxes.append((box.cost, box.volume_cm3(), box.name, box.pk, box))

        if not feasible_boxes:
            return None

        return min(feasible_boxes)[4]

    def __str__(self):
        return f"Order for {self.customer_name} on {self.created_at:%Y-%m-%d %H:%M}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('order', 'product')

    def __str__(self):
        return f"{self.product.name} x{self.quantity}"
