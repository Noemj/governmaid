from postapp.forms import PostForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.http import HttpResponse, Http404
from postapp.models import Post
from postapp.models import Vote

def create_post(request, *args, **kwargs):
	return render(request, 'create_post.html',{'extension':'template.html'})

def create_comment(request, *args, **kwargs):
	return render(request, 'create_comment.html', {'extension':'template.html'})

def process_create_post(request, *args, **kwargs):
	if request.method == 'POST':
		city = City.get_object(name=request.POST['city'])
    	post = Post(content=request.POST['content'],user=request.user,city=request.POST['city'],picture=request.FILES['picture'])
    	post.save()
    	return render(request, 'post.html',{'post':post})
    return HttpResponseRedirect('/')

def process_create_comment(request, *args, **kwargs):
	if request.method == 'POST':
		post = Post.get_object(name=request.POST['post'])
    	comment = Comment(post=post, content=request.POST['content'])
    	comment.save()
    	return render(request, 'post.html',{'post':post})
    return HttpResponseRedirect('/')

def vote(request, *args, **kwargs):
	if request.METHOD=='POST' and request.is_ajax():
		user = request.user
		pk = request.POST['post_pk']		
		vote_value = request.POST['vote_value']
		post = Post.objects.get(pk=pk)
		post += vote_value
		post.save()
		vote = Vote(user=user, post=post, vote=vote_status)
		vote.save()
		return "Success"
	else:
		return "Error"
		


