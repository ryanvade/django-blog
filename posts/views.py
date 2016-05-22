from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from posts.models import Post
from .forms import PostForm


def posts_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Created the post.")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = dict(form=form)
    return render(request, "post_form.html", context)


def posts_detail(request, id):
    instance = get_object_or_404(Post, id=id)
    context = dict(title=instance.title, instance=instance)
    return render(request, "post_detail.html", context)


def posts_list(request):
    queryset = Post.objects.all()
    context = dict(object_list=queryset, title="List is working")
    return render(request, "post_list.html", context)


def posts_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Edited the post.")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = dict(title=instance.title, instance=instance, form=form)
    return render(request, "post_form.html", context)


def posts_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Successfully Deleted the post.")
    return redirect("posts:list")
