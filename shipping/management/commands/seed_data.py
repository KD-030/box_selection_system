from django.core.management.base import BaseCommand

from shipping.models import Box, Product


class Command(BaseCommand):
    help = 'Seed the database with example products and shipping boxes.'

    def handle(self, *args, **options):
        Box.objects.all().delete()
        Product.objects.all().delete()

        products = [
            Product(name='Laptop', length_cm=35, width_cm=24, height_cm=5, weight_kg=2.5),
            Product(name='Coffee Maker', length_cm=30, width_cm=22, height_cm=18, weight_kg=4.2),
            Product(name='Gaming Console', length_cm=42, width_cm=30, height_cm=12, weight_kg=6.0),
            Product(name='Bookshelf', length_cm=80, width_cm=30, height_cm=25, weight_kg=15.0),
        ]
        Product.objects.bulk_create(products)

        boxes = [
            Box(name='Small Carton', internal_length_cm=40, internal_width_cm=30, internal_height_cm=20, max_weight_kg=8, cost=4.50),
            Box(name='Medium Carton', internal_length_cm=60, internal_width_cm=40, internal_height_cm=25, max_weight_kg=18, cost=7.25),
            Box(name='Large Carton', internal_length_cm=90, internal_width_cm=60, internal_height_cm=40, max_weight_kg=30, cost=12.75),
            Box(name='Extra Large Carton', internal_length_cm=120, internal_width_cm=80, internal_height_cm=60, max_weight_kg=50, cost=19.50),
        ]
        Box.objects.bulk_create(boxes)

        self.stdout.write(self.style.SUCCESS('Seed data created successfully.'))
