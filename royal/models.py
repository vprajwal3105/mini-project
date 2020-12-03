from django.db import models

# Create your models here.
class info(models.Model):
    login_id=models.IntegerField(null=True)
    name=models.CharField(max_length=50, verbose_name='username', default='DEFAULT VALUE')
    log_p=models.CharField(max_length=20, verbose_name='login_password', blank=True)

class customer(models.Model):
    customer_id=models. IntegerField(null=True)
    login_id=models.ForeignKey('info', on_delete=models.CASCADE)
    name=models.CharField(max_length=50, verbose_name='customer name')
    phone=models.BigIntegerField()
    address=models.CharField(max_length=100, verbose_name='customer address')

class comp_branch(models.Model):
   branch_id=models.IntegerField(null=True)
   address=models.CharField(max_length=100, verbose_name='company address')
   phone=models.BigIntegerField()
   email=models.CharField(max_length=100, verbose_name='company email')

class car_model(models.Model):
    model_id=models.IntegerField()
    branch_id=models.ForeignKey('comp_branch', on_delete=models.DO_NOTHING)
    ctype=models.CharField(max_length=20, verbose_name='car_type')
    name=models.CharField(max_length=20, verbose_name='model name')
    price=models.FloatField()
    fuel=models.CharField(max_length=20, verbose_name='fuel type')
    gear=models.CharField(max_length=20, verbose_name='gear type')
    seat=models.CharField(max_length=20, verbose_name='seating')
    mile=models.FloatField()


