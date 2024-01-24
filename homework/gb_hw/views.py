from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, get_object_or_404
import logging
from .models import Customer, Product, Order
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    return render(request, "gb_hw/base.html")


def about(request):
    """
    Для тестов добавил логировани, но логического смысла Exception не несет

    """
    try:
        logger.info('About page accessed')
        about_mi = "<h3> Привет, меня зовут Короткевич Артур. <br>" \
                   "<h4> Я junior python разработчик. <br>" \
                   "Я учусь в GeekBrains, на курсе Python-разработчик. <br>" \
                   "Участвовал в нескольких коммерческих проектах и стартапах. <br>"
        return HttpResponse(about_mi)
    except Exception as e:
        logger.exception(f'Error in about page: {e}')
        return HttpResponse("Oops, something went wrong.")


class CustomerList(View):
    def get(self, request):
        customers = Customer.objects.all()

        context = {'customers': customers}
        return render(request, 'gb_hw/customers.html', context)


class ProductList(View):
    def get(self, request):
        products = Product.objects.all()
        context = {'products': products}
        return render(request, 'gb_hw/products.html', context)


class OrderList(View):
    def get(self, request):
        # почему-то не работает get_object_or_404 в данном случае
        # orders = get_object_or_404(Order, pk=order)

        orders = Order.objects.all()

        context = {'orders': orders}
        return render(request, 'gb_hw/orders.html', context)


class OrderDetail(View):
    def get(self, request, order):
        orders = Order.objects.filter(pk=order)
        for i in orders:
            order_products = i.product.all()
            context = {
                'order': i,
                'order_products': order_products
            }

        return render(request, 'gb_hw/order_detail.html', context)


class OrdersCustomer(View):
    def get(self, request, customer):
        end_date = datetime.now()
        start_date = end_date - timedelta(days=360)

        customer = Customer.objects.get(pk=customer)
        orders = Order.objects.filter(customer_id=customer.pk, date_ordered__range=(start_date, end_date)).order_by(
            '-date_ordered')[:2]

        products_total = set()
        for order in orders:
            product = order.product.all()
            for i in product:
                products_total.add(i)

        context = {
            'customer': customer,
            'orders': orders,
            'products': products_total
        }

        return render(request, 'gb_hw/customer_detail.html', context)
