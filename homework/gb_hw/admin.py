from django.contrib import admin
from .models import Customer, Product, Order


@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(count=0)


@admin.action(description="Обнулить сумму заказа")
def reset_sum(modeladmin, request, queryset):
    queryset.update(total=0)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'description', 'price', 'count', 'date_added')
    ordering = ['-price', 'count']
    list_filter = ['date_added']
    search_fields = ['product_name', 'description']
    search_help_text = 'Введите название товара'
    readonly_fields = ['date_added']
    actions = [reset_quantity]

    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['product_name'],
            },),
        (
            'Приход',
            {
                'fields': ['price', 'count', 'date_added']
            }
        ), (

            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'описание',
                'fields': ['description', 'image']
            },
        )]


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'address', 'date_registration')
    ordering = ['-date_registration']
    search_fields = ['customer_name']
    search_help_text = 'Введите имя покупателя'
    readonly_fields = ['date_registration']

    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['customer_name', 'date_registration'],
            },),
        (
            'Данные клиента',
            {
                'fields': ['phone', 'address', 'email']
            }
        ), ]


class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'total')
    ordering = ['-total']
    list_filter = ['date_ordered']
    search_fields = ['customer']
    search_help_text = 'Введите имя покупателя'
    readonly_fields = ['date_ordered']
    actions = [reset_sum]

    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['customer'],
            },), (
            'Данные о заказе ',
            {
                'fields': ['product', 'total']
            }
        ), ]


admin.site.register(Product, ProductAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)

# Register your models here.
