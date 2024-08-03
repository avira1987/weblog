from django.contrib import admin
from django.urls import path

from Posts.views import post_list

urlpatterns = [
    path('ademin/',admin.site.urls),
    path('posts/',post_list, name= 'post-list'),
]