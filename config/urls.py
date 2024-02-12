"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from .settings import MEDIA_URL, MEDIA_ROOT
from posts.views import *
from account.views import  *
from post_category.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path("posts", posts_list, name="posts_list"),
    path("post/<int:pk>/", posts_detail, name="post_detail"),
    path("users/", user_list, name="user_list"),
    path("users/<int:pk>/", user_detail, name="user_detail"),
    path("comments_list/", posts_comments_list, name="comments_list"),
    path("comment/<int:pk>/", post_comment, name="post_comment"),
    path("categories", categories_list, name="categories_list"),
    path("categories/<int:pk>/", categories_detail, name="categories_detail")
]
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)