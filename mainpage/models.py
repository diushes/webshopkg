from django.db import models

# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    contacts = models.CharField(max_length=100)
    image = models.ImageField(max_length=120)
    date_pub = models.DateTimeField(auto_now_add= True)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date_pub']


