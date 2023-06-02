from django.contrib.auth.models import User
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


class ProfileImage(models.Model):
    profile_image = models.ImageField()


class UsersRecipesCreate(models.Model):
    title = models.CharField(max_length=150)
    recipe_picture = models.ImageField()
    body = models.TextField(max_length=10000)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #das erstellte Rezept wird einem bestimmten user zugewiesen, wenn der user gelöscht wird werden die Rezepte ebenfalls mitgeköscht.
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} | {self.author} | {self.date_created}'
