from django.db import models



# Create your models here.
class Customer(models.Model):
    id=models.AutoField(primary_key=True,max_length=10)
    customer_name=models.CharField(max_length=200)
    orderid=models.CharField(max_length=10,null=True)
    customer_email=models.EmailField()
    customer_contact=models.CharField(max_length=10,null=True)
    quetionstype=models.CharField(max_length=20,null=True)
    subject=models.CharField(max_length=50,null=True)
    description=models.CharField(max_length=400,default="")
    rate=models.IntegerField(null=True)
    #images=models.ImageField(upload_to='images')
    date_created=models.DateTimeField(auto_now_add=True,null=True, blank=True)


    def __str__(self):
        return self.customer_name