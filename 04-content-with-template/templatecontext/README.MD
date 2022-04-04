# Working with context in Django #

## Add data on view using context ##
```python
blog/views.py


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



```

## Modify view page ##
```html
<html>
<head>
    <title>This is main title</title>
</head>
<body>
    {% for post in posts %}
        <h1>{{ post.author }}</h1>
        <h2>{{ post.title }}</h2>
        <h3>{{ post.content }}</h3>
        <h4>{{ post.data_posted }}</h4>
    {% endfor %}
</body>
</html>
```