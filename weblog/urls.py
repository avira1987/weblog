"""
URL configuration for weblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from Posts.views_ import post_list,post_create,home,PostList,PostDetail, index
urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/',include('Posts.urls')),
    # path('',home,),
    # path('index/',index),
    # # path('posts/',post_list,name='post-list'),
    # # path('post/<int:pk>',post_detail,name='post-detail'),
    # path('posts/create/',post_create),
    # path('posts/',PostList.as_view()),
    # path('post/<int:pk>/',PostDetail.as_view())
    
]

