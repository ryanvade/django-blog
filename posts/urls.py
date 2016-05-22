from django.conf.urls import url

from posts import views as posts_view

urlpatterns = [
    url(r'^$', posts_view.posts_list),
    url(r'^create/$', posts_view.posts_create),
    url(r'^(?P<id>\d+)/$', posts_view.posts_detail),
    url(r'^update/$', posts_view.posts_update),
    url(r'^delete/$', posts_view.posts_delete),
]
