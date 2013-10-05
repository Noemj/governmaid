from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
	user = models.ForeignKey(User)
	score = models.IntegerField()
	content = models.TextField(max_length=1000, blank=False, null=False)

class Vote(models.Model):
	user = models.ForeignKey(User)
	vote = models.BooleanField()

class Comment(models.Model):
	post = models.ForeignKey(Post)
	content = models.TextField(max_length=1000, blank=False, null=False)
