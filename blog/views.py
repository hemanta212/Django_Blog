from django.shortcuts import render
from .models import Post
# Create your views here.


def home(requests):
    context = {
        'posts': Post.objects.all()
    }
    return render(requests, 'blog/home.html', context)


def about(requests):
    return render(requests, 'blog/about.html', {'title': 'About'})
