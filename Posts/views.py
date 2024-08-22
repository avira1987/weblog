from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from Posts.models import Post
from Posts.serializers import PostSerializer

# class PostListView(APIView):
#     def get(self, request):
#         post = Post.objects.all()
#         serializer  =PostSerializer(post, many=True)
#         return Response(serializer.data)
#     def post(self, request):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST
#                             )
# class PostDetailView(APIView):
#     def get(self, request,pk):
#         try:
#             post = Post.objects.get(pk=pk)
#         except Post.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
#     def put(self, request,pk):
#         try:
#             post = Post.objects.get(pk=pk)
#         except Post.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = PostSerializer(Post,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class PostDetailView(APIView):
#     def get_object(self, pk):
#         try:
#             post = Post.objects.get(pk=pk)
#         except Post.DoesNotExist:
#             raise Http404
#         return post
    
#     def get(self, request, pk):
#         post = self.get_object(pk)
#         serializer = PostSerializer(post)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         post = self.get_object(pk)
#         serializer = PostSerializer(post,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request,pk):
#         post = self.get_object(pk)
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
from rest_framework import generics
from rest_framework import mixins

# class PostListView(mixins.ListModelMixin,
#                    mixins.CreateModelMixin,
#                    generics.GenericAPIView):
#     queryset=Post.objects.all()
#     serializer_class = PostSerializer

#     def get(self, request,*arg, **kwargs):
#         return self.list(request,*arg, **kwargs)
    
#     def post(self, request, *arg, **kwargs):
#         return self.create(request,*arg, **kwargs)
    
# class PostDetailView(mixins.RetrieveModelMixin,
#                      mixins.UpdateModelMixin,
#                      mixins.DestroyModelMixin,
#                      generics.GenericAPIView):
#     queryset = Post.objects.all()
#     serializer_class=PostSerializer

#     def get(self, request,*arg, **kwargs):
#         return self.retrieve(request,*arg, **kwargs)
    
#     def put(self, request,*arg, **kwargs):
#         return self.update(request,*arg, **kwargs)
    
#     def delete(self, request,*arg, **kwargs):
#         return self.destroy(request,*arg, **kwargs)

# class PostListView(generics.ListCreateAPIview):
#     queryser= Post.objects.all()
#     serializer_class = PostSerializer

# class PostDetailView(generics.RetrieveupdateDestroyAPIView):
#     queryser= Post.objects.all()
#     serializer_class = PostSerializer
from rest_framework import viewsets
from rest_framework import permissions

class PostView(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


