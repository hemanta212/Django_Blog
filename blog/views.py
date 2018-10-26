from django.shortcuts import render

# Create your views here.
posts = [
    {
        'author': "Hemanta Sharma",
        'title': 'blog-post1',
        'content': 'codksjlfkjdfls',
        'date_posted': "2018-10-24",
    },
    {
        'author': "GOERA Sharma",
        'title': 'blog-post 2',
        'content': 'ckjdfls',
        'date_posted': "2016-10-24",
    },

]


def home(requests):
    context = {
        'posts': posts
    }
    return render(requests, 'blog/home.html', context)


def about(requests):
    return render(requests, 'blog/about.html', {'title': 'About'})
