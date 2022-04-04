from django.shortcuts import render
from django.http import HttpResponse

posts = [{
    'author': 'A',
    'title': 'Django Frame',
    'content': 'Post content',
    'data_posted': '2022/02/5 10:30:34 AM'
}]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)