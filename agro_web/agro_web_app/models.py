from django.db import models

class Algo(models.Model):
    
    comments = models.TextField(max_length = 500)

# Create your models here.
