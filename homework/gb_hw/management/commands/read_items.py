from django.core.management.base import BaseCommand
from gb_hw.models import Customer, Product, Order

class Command(BaseCommand):
    help = 'Просмотр всех данных по id '

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='id of item to show')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')

        customer = Customer.objects.filter(id=pk).first()
        if customer is not None:
            self.stdout.write(f'Клиент: {customer}')
        else:
            self.stdout.write(f'Клиент с id {pk} не найден')

        product = Product.objects.filter(id=pk).first()
        if product is not None:
            self.stdout.write(f'Продукт: {product} ')
        else:
            self.stdout.write(f'Продукт с id {pk} не найден')

        order = Order.objects.filter(id=pk).first()
        if order is not None:
            self.stdout.write(f'Заказ: {order} ')
        else:
            self.stdout.write(f'Заказ с id {pk} не найден')