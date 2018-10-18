from django.shortcuts import render
from django.http import HttpResponse

def posts(request):
    return render(request, 'news/posts.html')
