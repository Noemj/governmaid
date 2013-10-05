

def home(request, *args, **kwargs):
    
    return render(request, kwargs['template'],{'extension':'Welcome to Governmaid!'})