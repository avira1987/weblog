from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from Posts.models import Post
from Posts.serializers import PostSerializer

class PostListView(APIView):
    def get(self, request):
        post = Post.objects.all()
        serializer  =PostSerializer(post, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST
                            )
class PostDetailView(APIView):
    def get(self, request,pk):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PostSerializer(post)
        return Response(serializer.data)