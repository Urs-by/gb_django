from django.urls import path
from . import views
from .views import OrderList, ProductList, CustomerList, OrderDetail, OrdersCustomer


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('products/', ProductList.as_view(), name='products'),
    path('orders/', OrderList.as_view(), name='orders'),
    path('orders/<int:order>/', OrderDetail.as_view(), name='orders'),
    path('customers/', CustomerList.as_view(), name='customers'),
    path('customer_detail/<int:customer>/', OrdersCustomer.as_view(), name='customer_detail'),
    path('order_detail/<int:order>/', OrderDetail.as_view(), name='order_detail'),

]

