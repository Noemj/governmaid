from django.db import models

class Post(models.Model):
	score = models.IntegerField()
	content = models.TextField(max_length=1000, blank=False, null=False)