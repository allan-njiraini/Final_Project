from django.db import models

# Create your models here.



class Categories(models.Model):
    
    name = models.CharField(max_length=60)
    

    def __str__(self):
        return self.name
    

class Products(models.Model):
    
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="products")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Categories, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Email(models.Model):

    name = models.CharField(max_length=60)
    address = models.EmailField()
    message = models.TextField(max_length=300)

    def __str__(self):
        return self.name

