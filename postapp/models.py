from django.db import models
from django.contrib.auth.models import User
from cityapp import City


class Post(models.Model):
	city = models.ForeignKey(City,related_name='posts')
	user = models.ForeignKey(User,related_name='posts')
	score = models.IntegerField()
	content = models.TextField(max_length=1000, blank=False, null=False)

class Vote(models.Model):
	user = models.ForeignKey(User,related_name='votes')
	vote = models.BooleanField()

class Comment(models.Model):
	post = models.ForeignKey(Post,related_name='comments')
	content = models.TextField(max_length=1000, blank=False, null=False)
