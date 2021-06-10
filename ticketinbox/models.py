from django.db import models
from django.utils.timezone import now
from datetime import datetime
from index.models import Customer
from login.models import Executive

# Create your models here.

class Source(models.Model):
    src = (
        ('Email','Email'),
        ('Web-form','Web-form'),
        ('Social-media','Social-media')
    )
    source=models.CharField(primary_key=True, max_length=15,choices=src)
    def __str__(self):
        return self.source


class Status(models.Model):
    sta = (
        ('Closed','Closed'),
        ('Onhold','Onhold'),
        ('Open','Open'),
        ('Overdue','Overdue')
    )
    status=models.CharField(primary_key=True, max_length=15,choices=sta)
    def __str__(self):
        return self.status

        

class Priority(models.Model):
    pri = (
        ('High','High'),
        ('Medium','Medium'),
        ('Low','Low')
    )
    priority=models.CharField(primary_key=True, max_length=15,choices=pri)
    
    def __str__(self):
        return self.priority

class Ticket(models.Model):
    id = models.AutoField(primary_key=True)
    title =models.CharField(max_length=200)
    ticket_type=models.CharField(max_length=200)
    ticket_priority=models.ForeignKey(Priority,null=True,on_delete=models.SET_NULL)
    source=models.ForeignKey(Source,null=True,on_delete=models.SET_NULL)
    ticket_status=models.ForeignKey(Status,null=True,on_delete=models.SET_NULL)
    assigned_dep=models.CharField(max_length=30,null=True)
    created_on=models.DateTimeField(null=True)
    due_date=models.DateTimeField(null=True)
    assigned_to=models.ForeignKey(Executive,max_length=10,null=True,on_delete=models.SET_NULL)
    ticket_rating=models.CharField(max_length=10,null=True)
    solution=models.CharField(max_length=200,null=True)
    customer_id = models.ForeignKey(Customer,null=True,blank=True,on_delete=models.SET_NULL)
    process= models.CharField(max_length=20,null=True)


    def __str__(self):
        return '{}{}{}'.format(self.title, self.ticket_status, self.ticket_type)

class Product(models.Model):
    ctgr=(
        ('clothing','clothing'),
        ('accessories','accessories'),
        ('footwear','footwear')

    )
    id=models.IntegerField(primary_key=True)
    product_name=models.CharField(max_length=200)
    product_catogary=models.CharField(max_length=200,choices=ctgr)
    def _str_(self):
        return self.product_name




