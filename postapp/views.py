# Create your views here.
from postapp.forms import PostForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.http import HttpResponse, Http404
from postapp.models import Post

def create(request, *args, **kwargs):
	return render(request, 'create_post.html',{'extension':'template.html'})


def process_create(request, *args, **kwargs):
	if request.method == 'POST':
		city = City.get_object(name=request.POST['city'])
    	post = Post(content=request.POST['content'],user=request.user,city=request.POST['city'],picture=request.FILES['picture'])
    	post.save()
    	return render(request, 'post.html',{'post':post})
    return HttpResponseRedirect('/')