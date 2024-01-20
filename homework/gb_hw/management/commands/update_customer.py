from django.core.management.base import BaseCommand
from gb_hw.models import Customer, Product, Order


class Command(BaseCommand):
    help = 'Update items'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='id of item to delete')
        parser.add_argument('field', type=str, help='customers, products, orders')
        parser.add_argument('new_value', type=str, help='field to update')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        field = kwargs.get('field')
        new_value = kwargs.get('new_value')


        customer = Customer.objects.filter(id=pk).first()
        if customer is not None:
            # if field == 'customer_name':
            #     customer.customer_name = new_value
            # elif field == 'email':
            #     customer.email = new_value
            # elif field == 'phone':
            #     customer.phone = new_value
            # elif field == 'address':
            #     customer.address = new_value
            # else:
            #     self.stdout.write('Неверное поле')

            setattr(customer, field, new_value)
            customer.save()
            self.stdout.write(f'Клиент {customer} обновлен')
        else:
            self.stdout.write(f'Клиент с id {pk} не найден')