from django.contrib import admin
from .models import Products,Order

# Register your models here.

class Product_items(admin.ModelAdmin):
    list_display=('title','price','discount_price','category','description')
    search_fields=('title',)

admin.site.site_header="E-commerce Site"
admin.site.site_title="ABC Shop"
admin.site.index_title="Manage ABC Shop"
admin.site.register(Products,Product_items)
admin.site.register(Order)
