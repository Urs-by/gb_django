from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, get_object_or_404
import logging
from .models import Customer, Product, Order
from datetime import datetime, timedelta
from .forms import UpdateProductForm
from django.core.files.storage import FileSystemStorage

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
        form = UpdateProductForm()
        message = "Для изменения данных заполните форму"
        products = Product.objects.all()
        context = {'products': products, 'form': form, 'message': message}
        return render(request, 'gb_hw/products.html', context)

    def post(self, request):
        form = UpdateProductForm(request.POST, request.FILES)
        if form.is_valid():
            product_id = form.cleaned_data['id']
            product = Product.objects.filter(id=product_id).first()
            if product:
                product.product_name = form.cleaned_data['product_name']
                product.description = form.cleaned_data['description']
                product.price = form.cleaned_data['price']
                product.count = form.cleaned_data['count']

                product.image = form.cleaned_data['image']
                fs = FileSystemStorage()
                fs.save(product.image.name, product.image)
                product.save()
            #form.save()
                message = "Данные успешно обновлены"
                products = Product.objects.all()
                context = { 'products': products, 'form': form, 'message': message}
                return render(request, 'gb_hw/products.html', context)
            else:
                products_all = Product.objects.all()
                message = f"Товара с указанным ID={product_id} нет в базе данных"
                context = {'products': products_all, 'form': form, 'message': message}
                return render(request, 'gb_hw/products.html', context)


        # else:
        #     # Действия при валидации формы не удалась
        #     products = Product.objects.all()
        #     message = "Возникла ошибка. Пожалуйста, заполните форму корректно."
        #     context = {'products': products, 'form': form, 'message': message}
        #     return render(request, 'gb_hw/products.html', context)





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
    def get(self, request, customer, delta=360):
        end_date = datetime.now()
        start_date = end_date - timedelta(days=delta)

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
