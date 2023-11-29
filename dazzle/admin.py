from django.contrib import admin
from dazzle.models import Categories, Products


# Register your models here.

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    
admin.site.register(Categories, CategoriesAdmin)

class ProductsAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

admin.site.register(Products, ProductsAdmin)


