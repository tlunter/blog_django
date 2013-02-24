from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from app.decorators import is_staff
from posts.models import Post
from comments.models import Comment
from comments.forms import CommentCreationForm, CommentDeletionForm

def index(request, user_id):
    comments = Comment.objects.filter(created_by__id = user_id)
    return render(request, 'comments/index.html', { 'comments': comments })

def show(request, comment_id):
    try:
        comment = Comment.objects.select_related().get(pk = comment_id)
    except Comment.DoesNotExist:
        raise Http404

    return render(request, 'comments/show.html', { 'comment': comment })

@login_required
def new(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404

    if request.method == "POST":
        form = CommentCreationForm(request.POST, initial={'post': post})

        if form.is_valid():
            comment = form.save(request.user)
            return HttpResponseRedirect(reverse('posts.views.show', args=[post.pk]))
    else:
        form = CommentCreationForm(initial={'post': post})

    return render(request, 'comments/new.html', { 'form': form, 'post': post })

@login_required
def edit(request, comment_id):
    try:
        comment = Comment.objects.get(pk=comment_id)
    except Comment.DoesNotExist:
        raise Http404

    if not request.user.is_staff or comment.created_by != request.user:
        return HttpResponseRedirect(reverse('posts.views.show', args=[comment.post.pk]))

    if request.method == "POST":
        form = CommentCreationForm(request.POST, instance=comment)

        if form.is_valid():
            comment = form.save(request.user)
            return HttpResponseRedirect(reverse('posts.views.show', args=[comment.post.pk]))

    else:
        form = CommentCreationForm(instance=comment)

    return render(request, 'comments/edit.html', { 'form': form })

@login_required
def delete(request, comment_id):
    try:
        comment = Comment.objects.select_related().get(pk=comment_id)
    except Comment.DoesNotExist:
        raise Http404 

    if not request.user.is_staff or comment.created_by != request.user:
        return HttpResponseRedirect(reverse('posts.views.show', args=[comment.post.pk]))

    if request.method == "POST":
        form = CommentDeletionForm(request.POST)

        if form.is_valid():
            comment.delete();
            return HttpResponseRedirect(reverse('posts.views.show', args=[comment.post.pk]))
    else:
        form = CommentDeletionForm()

    return render(request, 'comments/delete.html', { 'form': form, 'form_url': reverse('comments.views.delete', args=[comment.pk]) })

