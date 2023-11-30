from django.forms import ModelForm
from dazzle.models import Categories, Products, Email



class CategoriesForm(ModelForm):
    class Meta:
        model = Categories
        fields = ["name"]

class ProductsForm(ModelForm):
    class Meta:
        model = Products
        fields = ["name", "image", "price", "category"]


class EmailForm(ModelForm):
    class Meta:
        model = Email
        fields = ["name", "address", "message"]


