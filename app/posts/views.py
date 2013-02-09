from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from app.decorators import is_staff
from posts.models import Post
from posts.forms import PostCreationForm, PostDeletionForm
from comments.models import Comment

def index(request):
    posts = Post.objects.all()

    if not request.user.is_staff:
        posts = posts.filter(visible=True)

    posts = posts.order_by('-created_on')

    return render(request, 'posts/index.html', { 'posts': posts })

def show(request, post_id):
    try:
        post = Post.objects.select_related().get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404

    return render(request, 'posts/show.html', { 'post': post })

@is_staff(permission='posts.add_post')
def new(request):
    if request.method == "POST":
        form = PostCreationForm(request.POST)

        if form.is_valid():
            post = form.save(request.user)
            return HttpResponseRedirect(reverse('posts.views.show', args=[post.pk]))
    else:
        form = PostCreationForm()

    return render(request, 'posts/new.html', { 'form': form })

def edit(request, post_id):
    try:
        post = Post.objects.select_related().get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404 

    if not request.user.is_staff or post.created_by != request.user:
        return HttpResponseRedirect(reverse('posts.views.show', args=[post.pk]))

    if request.method == "POST":
        form = PostCreationForm(request.POST, instance=post)

        if form.is_valid():
            post = form.save(request.user)
            return HttpResponseRedirect(reverse('posts.views.show', args=[post.pk]))

    else:
        form = PostCreationForm(instance=post)

    return render(request, 'posts/edit.html', { 'form': form })

def delete(request, post_id):
    try:
        post = Post.objects.select_related().get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404 

    if not request.user.is_staff or post.created_by != request.user:
        return HttpResponseRedirect(reverse('posts.views.show', args=[post.pk]))

    if request.method == "POST":
        form = PostDeletionForm(request.POST)

        if form.is_valid():
            post.delete();
            return HttpResponseRedirect(reverse('posts.views.index'))
    else:
        form = PostDeletionForm()

    return render(request, 'posts/delete.html', { 'form': form, 'form_url': reverse('posts.views.delete', args=[post.pk]) })
