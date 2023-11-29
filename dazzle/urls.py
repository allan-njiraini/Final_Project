from django.urls import path
from . import views

app_name = 'dazzle'
urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('gallery', views.gallery, name='gallery'),
    path('blog', views.blog, name='blog'),
    path('create_categories', views.create_categories, name='create_categories' ),
    path('create_products', views.create_products, name='create_products' ),
    path('category/<str:name>', views.categories, name='category')

]

