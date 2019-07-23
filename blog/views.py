from django.shortcuts import render
from .models import blog

# Create your views here.

def allblogs(request):
    blogs = blog.objects
    return render(request, 'blog/blog-list.html', {'blogs':blogs})


def blogpost(request):
    return render(request, 'blog/blog-post.html')