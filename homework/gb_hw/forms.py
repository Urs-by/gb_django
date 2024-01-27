from django import forms
from .models import Product


# class UpdateProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ['product_name', 'description', 'price', 'count']


class UpdateProductForm(forms.Form):
    id = forms.IntegerField(max_value=99999)
    product_name = forms.CharField(max_length=50)
    description = forms.CharField(max_length=200)
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    count = forms.IntegerField(max_value=99999)
    image = forms.ImageField()