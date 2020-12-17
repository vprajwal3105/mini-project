from django.db import models

# Create your models here.

class car_model(models.Model):

    model_id= models.IntegerField(primary_key=True)
    car_type= models.TextField()
    model_name= models.TextField()
    