from django.db import models
from django import forms
# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=200)
    orderid=models.CharField(max_length=10)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    quetionstype=models.CharField(max_length=20)
    subject=models.CharField(max_length=50)
    description=models.CharField(max_length=400,default="")
    rate=models.IntegerField(null=True)
    #images=models.ImageField(upload_to='images')
    date_created=models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    rating = models.CharField(max_length=10,null=True,blank=True)
    text = models.CharField(max_length=200,null=True,blank=True)
    name = models.CharField(max_length=50,null=True)
    email = models.EmailField(null=True,blank=True)

    def __str__(self):
        return self.email
    
