from django.core.management.base import BaseCommand
from gb_hw.models import Customer, Product, Order


class Command(BaseCommand):
    help = 'Обновление продуктов'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='id of item to delete')
        parser.add_argument('field', type=str, help='customers, products, orders')
        parser.add_argument('new_value', type=str, help='field to update')

    def handle(self, *args, **kwargs):

        pk = kwargs.get('pk')
        field = kwargs.get('field')
        new_value = kwargs.get('new_value')

        product = Product.objects.filter(id=pk).first()

        if product is not None:
            setattr(product, field, new_value)
            product.save()
            self.stdout.write(f'Продукт {product} обновлен')
        else:
            self.stdout.write(f'Продукт с id {pk} не найден')