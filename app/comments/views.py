from django.shortcuts import render
from posts.models import Post
from comments.models import Comment
from django.http import Http404

def index(request, user_id):

    comments = Comment.objects.filter(created_by__id = user_id)
    return render(request, 'comments/index.html', { 'comments': comments })

def show(request, comment_id):
    try:
        comment = Comment.objects.select_related().get(pk = comment_id)
    except Comment.DoesNotExist:
        raise Http404

    return render(request, 'comments/show.html', { 'comment': comment })

