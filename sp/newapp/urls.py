from django.urls import path    
from . import views

urlpatterns = [

    path('index',views.index,name='index'),
    path('signup',views.signup, name='signup'),
    path('dash',views.dashboard, name='dash'),
    path('',views.login,name='login'),
    path('about',views.about, name='about'),
    path('product',views.product, name='product'),
    path('contact',views.contact, name='contact'),
]