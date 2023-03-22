from django.http import Http404
from django.shortcuts import render
from .models import Post
from django.db.models import F


def view_post(request, slug):
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        raise Http404("Poll does not exist")
    
    post.view_count = F('view_count') + 1
    post.save()
    post.refresh_from_db()
    
    return render(request, 'publish/post.html', context={'post': post})
