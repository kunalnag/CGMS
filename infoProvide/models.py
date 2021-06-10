from django.db import models

class Provider(models.Model):
    id = models.AutoField(primary_key=True)
    cat=(
        ('Alert','Alert'),
        ('Warning','Warning')
    )
    category =models.CharField(max_length=30,null=True,choices=cat)
    title =models.CharField(max_length=200)
    description =models.TextField()

    def __str__(self):
        return self.title


   
    
