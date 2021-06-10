from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Executive(models.Model):
    id=models.AutoField(primary_key=True,max_length=20,default="")
    executive_name=models.CharField(max_length=50,null=True,blank=True)
    executive_username=models.CharField(max_length=50,null=True,blank=True)
    executive_email=models.EmailField()
    executive_pass=models.CharField(max_length=32,null=True,blank=True)
    executive_contact=models.IntegerField(null=True,blank=True)
    executive_dep=models.CharField(max_length=100,null=True,blank=True)
    executive_level=models.CharField(max_length=20,null=True,blank=True)
    executive_status=models.CharField(max_length=20,null=True,blank=True)
    # ticket_assigned=models.ForeignKey(Ticket, on_delete=models.CASCADE,null=True)
    assigned=models.IntegerField(null=True,blank=True)
    resolved=models.IntegerField(null=True,blank=True)
    sla = models.IntegerField(null=True,blank=True)
    total_responses = models.IntegerField(null=True,blank=True)
    avg_response = models.IntegerField(null=True,blank=True)
    avg_resolution=models.IntegerField(null=True,blank=True)
    rating=models.IntegerField(null=True,blank=True)


    def _str_(self):
        return self.executive_name
