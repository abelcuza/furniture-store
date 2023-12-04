from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    img_url = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    stock_quantity = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    img_url = models.CharField(max_length=255, null=True)
    rate = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)

    class Meta:
        ordering = ['-rate']

    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=11, null=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    order_date = models.DateTimeField(null=True)
    shipping_date = models.DateTimeField(null=True)
    shipping_address = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f"{self.customer.full_name} - {self.order_date}"


class Deals(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    number = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.product.name

    @property
    def price(self):
        return self.product.price - (self.product.price * self.number)

    @property
    def porcent(self):
        return self.number * 100
