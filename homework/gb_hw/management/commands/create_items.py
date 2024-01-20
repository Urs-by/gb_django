from django.core.management.base import BaseCommand
from gb_hw.models import Customer, Product


class Command(BaseCommand):
    help = 'Создание фейков в базе данных'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count of customers to create')

    def handle(self, *args, **kwargs):
        pk = kwargs['count']


        for i in range(pk):
            customer = Customer(customer_name=f'Продавец_{i}', email=f'mail{i}@example.com',
                                phone=f'749912311{i}',
                                address=f'г.Минск, ул. Кирова {i}, д. {pk - i}, кв{i * 3}')
            customer.save()
            self.stdout.write(f'{customer}')

            product = Product(product_name=f'Продукт_{i}', description=f'Описание продукта {i}',
                              price=i * 10, count=f'{i}' * 2)
            product.save()
            self.stdout.write(f'{product}')


