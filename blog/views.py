from django.shortcuts import render

# Create your views here.

def allblogs(request):
    return render(request, 'blog/blog-list.html')