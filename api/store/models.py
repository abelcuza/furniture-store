from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_length=8, decimal_places=2)
    stock_quantity = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=11)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    order_date = models.DateTimeField()
    shipping_date = models.DateTimeField()
    shipping_address = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.customer.name} - {self.order_date}"
