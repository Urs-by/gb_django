from django.urls import path
from . import views
from .views import Order, ProductList

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('orders/', Order.as_view(), name='orders'),
    path('products/', ProductList.as_view(), name='products'),
    # path('orders/<uuid:pk>/', order_detail)
]
