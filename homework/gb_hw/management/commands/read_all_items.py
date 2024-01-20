from django.core.management.base import BaseCommand
from gb_hw.models import  Customer, Product, Order


class Command(BaseCommand):
    help = ('Команда выводит список всех сущностей в зависимости от аргумента '
            'в качестве аргументов надо ввести строку "customers" или "products" или "orders"')

    def add_arguments(self, parser):
        parser.add_argument('entity', type=str, help='customers, products, orders')

    def handle(self, *args, **kwargs):
        entity = kwargs.get('entity')
        if entity is None:
            self.stdout.write('Не указана сущность')

        elif entity == 'customers':
            customers = Customer.objects.all()
            for customer in customers:
                self.stdout.write(f'Клиент: {customer}')

        elif entity == 'products':
            products = Product.objects.all()
            for product in products:
                self.stdout.write(f'Продукт: {product}')

        elif   entity == 'orders':
            orders = Order.objects.all()
            for order in orders:
                self.stdout.write(f'Заказ: {order}')
        else:
            self.stdout.write('Неизвестная сущность')