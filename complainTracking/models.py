from django.db import models
from ..ticketinbox import *

# Create your models here.

class Solution(models.Model):
    ticket_id=models.ForeignKey
    solution=models.CharField(max_length=500)


    def __str__(self):
        return self.ticket_id


