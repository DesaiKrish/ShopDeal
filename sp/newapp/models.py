from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import datetime


class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, unique=True)

class User(models.Model):
    cust_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=40)
    address = models.CharField(max_length=100)
    phone_num = PhoneNumberField()

class Seller(models.Model):
    seller_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=200, default='', blank=True, null=True)
    category = models.ForeignKey(Category, to_field="name", on_delete=models.CASCADE)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=8)
    seller_name = models.ForeignKey(Seller, to_field="name", on_delete=models.CASCADE, default='')

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_date = models.DateField()
    total_price = models.DecimalField(decimal_places=2, max_digits=8)
    customer = models.ForeignKey(User, to_field="cust_id", on_delete=models.CASCADE)

class OrderItem(models.Model):
    order_item_id = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    order = models.ForeignKey(Order, to_field="order_id", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    customer = models.ForeignKey(User, to_field="cust_id", on_delete=models.CASCADE)

class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    payment_date = models.DateField()
    payment_method = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    customer = models.ForeignKey(User, to_field="cust_id", on_delete=models.CASCADE)

class Shipment(models.Model):
    ship_id = models.AutoField(primary_key=True)
    ship_date = models.DateField()
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pin_code = models.CharField(max_length=20)
    country = models.CharField(max_length=50)
    order = models.ForeignKey(Order, to_field="order_id", on_delete=models.CASCADE)

# Create your models here.