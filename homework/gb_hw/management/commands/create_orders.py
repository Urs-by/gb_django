from django.core.management.base import BaseCommand
from gb_hw.models import Customer, Product, Order
import random


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        costumers = Customer.objects.all()
        products = Product.objects.all()

        for costumer in costumers:
            order = Order(customer=costumer, total=0)  # Создаем заказ для клиента
            order.save()
            for i in range(random.randint(1, 5)):
                product = random.choice(products)
                order.product.add(product)  # Добавляем товар в заказ
                order.total += product.price
            order.save()  # Сохраняем заказ
        self.stdout.write(self.style.SUCCESS('Фейковые заказы успешно созданы'))