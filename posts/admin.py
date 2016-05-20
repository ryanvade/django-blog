from django.contrib import admin

from posts.models import Post


class PostModelAdmin(admin.ModelAdmin):
    # list_display is the array of attributes that will be displayed in the admin console
    list_display = ["title", "updated", "timestamp"]
    # list_display_links is the array of attributes in the admin console that will be links
    list_display_links = ["updated", "timestamp"]
    # search_fields it the array of attributes that are searchable in the admin console
    search_fields = ["title", "content"]
    # list_editable is the array of attributes that are editable in the admin console
    list_editable = ["title"]

    class Meta:
        model = Post


admin.site.register(Post, PostModelAdmin)
