from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    
    def __str__(self) -> str:
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Genders(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name


class Products(models.Model):
    company = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    gender = models.ForeignKey(Genders, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.company
    

class Comment(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    

