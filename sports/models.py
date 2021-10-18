from django.db import models

# Create your models here.
class sports(models.Model):      # Creating model class
    name = models.CharField(max_length=20) 
    sport = models.CharField(max_length=10)
    age = models.IntegerField()  
    def __str__(self):  
        return self.name