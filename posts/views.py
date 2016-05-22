from django.shortcuts import render, get_object_or_404

from posts.models import Post


def posts_create(request):
    context = dict(title="Create")
    return render(request, "index.html", context)


def posts_detail(request, id):
    instance = get_object_or_404(Post, id=id)
    context = dict(title=instance.title, instance=instance)
    return render(request, "post_detail.html", context)


def posts_list(request):
    queryset = Post.objects.all()
    context = dict(object_list=queryset, title="List is working")
    return render(request, "index.html", context)


def posts_update(request):
    context = dict(title="Update is working")
    return render(request, "index.html", context)


def posts_delete(request):
    context = dict(title="Delete is working")
    return render(request, "index.html", context)
