from django.db import models
from django.contrib.auth.models import User
from PIL import Image

def file_name(instance, filename):
    return 'postpics/'+instance.pk+"profile.jpg"

class Post(models.Model):
	city = models.ForeignKey('cityapp.City',related_name='posts')
	user = models.ForeignKey(User,related_name='posts')
	score = models.IntegerField()
	picture = models.ImageField(upload_to=file_name, max_length=200, blank=True, null=True)
	content = models.TextField(max_length=1000, blank=False, null=False)
	
class Vote(models.Model):
	user = models.ForeignKey(User,related_name='votes')
	vote = models.BooleanField()

class Comment(models.Model):
	post = models.ForeignKey(Post,related_name='comments')
	content = models.TextField(max_length=1000, blank=False, null=False)
