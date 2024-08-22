from django.urls import path, include
# from Posts.views import PostListView ,PostDetailView
from Posts.views import PostView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'',PostView, basename='posts')

urlpatterns=[
     path('',include(router.urls)),
    # path('', PostListView.as_view()),
    # path('<int:pk>/',PostDetailView.as_view()),
    # path('posts',)
    # path('',PostView.as_view({'get':'list','get':'create'})),
    # path('<int:pk>/', PostView.as_view({'get':'retrieve', 'put':'updatae','delete':'destroy'}))
   
] 

