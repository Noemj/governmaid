from django.db import models
from django.contrib.auth.models import User


def file_name(instance, filename):
    return instance.pk+"/profile/"+year+"/"+month+"/"+day+"/"+hour+"/"+minute+"/"+second+"/profile.jpg"

class Post(models.Model):
	user = models.ForeignKey(User)
	score = models.IntegerField()
	#picture = models.ImageField(upload_to=file_name, max_length=200, blank=True, null=True)
	content = models.TextField(max_length=1000, blank=False, null=False)
	
class Vote(models.Model):
	user = models.ForeignKey(User)
	vote = models.BooleanField()

class Comment(models.Model):
	post = models.ForeignKey(Post)
	content = models.TextField(max_length=1000, blank=False, null=False)
