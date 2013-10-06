from django.db import models
from django.contrib import admin

class City(models.Model):
	name = models.CharField(max_length=50)
	mayor = models.CharField(max_length=100,null=True, blank=True)

admin.site.register(City)
