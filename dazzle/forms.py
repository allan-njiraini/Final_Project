from django.forms import ModelForm
from dazzle.models import Categories, Products



class CategoriesForm(ModelForm):
    class Meta:
        model = Categories
        fields = ["name"]

class ProductsForm(ModelForm):
    class Meta:
        model = Products
        fields = ["name", "image", "price", "category"]
