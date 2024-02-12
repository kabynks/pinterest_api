from django.contrib.admin import *

from account import admin
from .models import *
from post_category.models import PostCategory
@admin.register(Post)
class PostAdmin(ModelAdmin):
    list_display = ('id', "title", "user", "post_category", "created",)
    list_display_links = ("id", "user", "created")

@admin.register(PostCategory)
class PostCategoryAdmin(ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
@admin.register(PostComments)
class PostCommentsAdmin(ModelAdmin):
    list_display = ("id", "user", "post")
    list_display_links = ("id", "user")


