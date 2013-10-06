from django.db import models
from django.contrib import admin

class City(models.Model):
	name = models.CharField(max_length=50)

admin.site.register(City)
