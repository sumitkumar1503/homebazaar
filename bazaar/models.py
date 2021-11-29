from datetime import date
from django.db import models
from django.contrib.auth.models import User



class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    address=models.CharField(max_length=500)
    mobile = models.CharField(max_length=40,null=True)
    
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name



class Category(models.Model):
    englishname=models.CharField(max_length=300)
    hindiname=models.CharField(max_length=300)
    photo= models.ImageField(upload_to='images/categories/',null=True,blank=True)
    def __str__(self):
        return self.englishname


class Product(models.Model):
    englishname=models.CharField(max_length=300)
    hindiname=models.CharField(max_length=300)
    photo= models.ImageField(upload_to='images/products/',null=True,blank=True)
    categoryid=models.PositiveIntegerField(null=True)
    categoryname=models.CharField(max_length=200,null=True)
    price=models.PositiveIntegerField(null=True)
    quantity=models.CharField(max_length=100)
    def __str__(self):
        return self.englishname

class Order(models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
    product=models.ForeignKey(Product, on_delete=models.CASCADE,null=True)
    category=models.ForeignKey( Category,on_delete=models.CASCADE,null=True)
    price=models.PositiveIntegerField(null=True)
    mobile=models.CharField(max_length=20,null=True)
    address=models.CharField(max_length=500,null=True)
    date=models.DateField(auto_now=True)