from django.db import models


# Create your models here.

class UserCredentials(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    date_created = models.DateTimeField(auto_now_add=True)


class Groceries(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ProductList(models.Model):
    product_names = models.ManyToManyField(Groceries)
    created_at = models.DateTimeField(auto_now_add=True)

