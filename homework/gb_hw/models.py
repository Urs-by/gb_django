from django.db import models


class Customer(models.Model):
    customer_name = models.CharField(max_length=200, null=True)
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.CharField(max_length=200, null=True)
    date_registration = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.customer_name}, {self.email}, {self.date_registration}'


class Product(models.Model):
    product_name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product_name}, цена: {self.price}, количество: {self.count}'

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    product = models.ManyToManyField(Product)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.pk}, {self.customer}, {self.total}'
