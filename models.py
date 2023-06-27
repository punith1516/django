from django.db import models

# Create your models here.
class Feature():
    name=models.CharField(max_length=100)
    details=models.CharField(max_length=500)


    
    