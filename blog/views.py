from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
# Create your views here.

# def index(request):
#     #Use the django ORM framework to get the data 
#     posts = Post.objects.all()
#     return render(request, 'blog/index.html', {'posts':posts})


def index(request):
    #Use the django ORM framework to get the data 
    posts = Post.objects.all()
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            #Get the instance form the save but not commit the data to the DB, in mem
            instance = form.save(commit=False)
            #Set the author for the created post form
            instance.author = request.user
            #Save to the DB with the author is the logon user
            instance.save()
            #after save OK, redirect the page to the index page, the names are defined in the urls.py
            return redirect('index')
    else:
        form = PostForm()

    context = {
        'posts':posts,
        'form': form
    }
    return render(request, 'blog/index.html', context)

def about(request):
    return render(request, 'blog/about.html', {})