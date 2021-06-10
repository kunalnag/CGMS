from django.db import models

    # Create your models here.
class Club(models.Model):
    channel_name = models.CharField(max_length=220)
    total_query = models.IntegerField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return "{}-{}".format(self.channel_name, self.total_query)



      

        
            
        

        
