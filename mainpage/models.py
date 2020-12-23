from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    contacts = models.CharField(max_length=100)
    image = models.ImageField(max_length=120)
    date_pub = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date_pub']


class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.CharField(max_length=50)
    image = models.ImageField(max_length=120)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


