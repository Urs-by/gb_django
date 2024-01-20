from django.core.management.base import BaseCommand
from gb_hw.models import Customer, Product, Order


class Command(BaseCommand):
    help = ('Удаляет объект, если он существует'
            'в качестве аргументов надо ввести id и строку "customers" или "products" или "orders')

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='id of item to delete')
        parser.add_argument('entity', type=str, help='customers, products, orders')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        entity = kwargs.get('entity')

        if entity == 'customers':
            customer = Customer.objects.filter(id=pk).first()
            if customer is not None:
                customer.delete()
                self.stdout.write(f'Клиент: {customer} удален')
            else:
                self.stdout.write(f'Клиент с id {pk} не найден')
        elif entity == 'products':
            product = Product.objects.filter(id=pk).first()
            if product is not None:
                product.delete()
                self.stdout.write(f'Продукт : {product} удален')
            else:
                self.stdout.write(f'Продукт с id {pk} не найден')
        elif entity == 'orders':
            order = Order.objects.filter(id=pk).first()
            if order is not None:
                order.delete()
                self.stdout.write(f'Заказ : {order} удален')
            else:
                self.stdout.write(f'Заказ с id {pk} не найден')

        else:
            self.stdout.write('Введены неверные данные')