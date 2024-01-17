from django.core.management.base import BaseCommand
from gb_hw.models import Customer, Product


class Command(BaseCommand):
    help = 'Create a new customer'

    def add_base_argument(self, parser, *args, **kwargs):
        parser.add_argument('count', type=int, help='Count of customers to create')

    def hendle(self, *args, **kwargs):
        count = kwargs['count']
        for i in range(count):
            customer = Customer(customer_name=f'Продавец_{i}', email=f'mail{i}@example.com',
                                phone=f'749912311{i}',
                                address=f'г.Минск, ул. Кирова {i}, д. {count - i}, кв{i * 3}')
            customer.save()
            self.stdout.write(f'{customer}')

            product = Product(product_name=f'Продукт_{i}', description=f'Описание продукта {i}',
                              price=i * 100, count=f'{i}' * 10)
            product.save()
            self.stdout.write(f'{customer}')



