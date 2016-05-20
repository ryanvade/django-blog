from django.shortcuts import render


def posts_create(request):
    context = dict(title="Create")
    return render(request, "index.html", context)


def posts_detail(request):
    context = dict(title="Detail is working")
    return render(request, "index.html", context)


def posts_list(request):
    context = dict(title="List is working")
    return render(request, "index.html", context)


def posts_update(request):
    context = dict(title="Update is working")
    return render(request, "index.html", context)


def posts_delete(request):
    context = dict(title="Delete is working")
    return render(request, "index.html", context)
