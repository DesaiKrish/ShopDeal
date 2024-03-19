from django.urls import path    
from . import views

urlpatterns = [

    path('sign',views.sign, name='sign'),
    path('', views.login, name='login'),
    path('index', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('product', views.product, name='product'),
    path('service', views.service, name='service'),
]