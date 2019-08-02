from django.shortcuts import render, get_object_or_404
from .models import blog

# Create your views here.

def allblogs(request):
    blogs = blog.objects
    return render(request, 'blog/blog-list.html', {'blogs':blogs})


def blogpost(request, blog_id):
    blogpost = get_object_or_404(blog, pk=blog_id)
    return render(request, 'blog/blog-post.html', {'blogpost':blogpost})
