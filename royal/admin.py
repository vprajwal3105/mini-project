from django.contrib import admin

# Register your models here.
from . import models
admin.site.register(models.info)
admin.site.register(models.customer)
admin.site.register(models.comp_branch)
admin.site.register(models.car_model)