from django.core.management.base import BaseCommand
from barchart.models import Product

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        Product.objects.create(name='iPhone 13', rating=4.6)
        Product.objects.create(name='Samsung Galaxy S22', rating=4.4)
        Product.objects.create(name='Google Pixel 6 Pro', rating=4.5)
        Product.objects.create(name='Sony PlayStation 5', rating=4.8)
        Product.objects.create(name='Nintendo Switch', rating=4.7)