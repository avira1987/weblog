from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,get_object_or_404
from Posts.models import Post,Comment
from Posts.forms import PostForm
from django.http import HttpResponse,HttpResponseRedirect, HttpResponseNotFound

from django.views.generic import DetailView, ListView

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from Posts.serializers import PostSerializer
# Create your views here.

@api_view(['GET','POST'])
def home(request):

    return Response({'name':'avx'},status=status.HTTP_200_OK)

def post_list(request):
    posts = Post.objects.all()
    context= {'posts':posts}
    return  render(request, 'posts/post_list.html', context= context)

# def post_detail(request,pk):
    # try:
    #     post = Post.objects.get(pk=pk)
    # except Post.DoesNotExist:
    #     return HttpResponseNotFound("Post is not exist")
    # post=get_object_or_404(Post, pk=pk)
    # comments = Comment.objects.filter(post=post)
    # context= {'post':post, 'comments':comments}
    # return render(request,'posts/post_detail.html',context=context)

def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            Post.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/posts/')
    else:
        form = PostForm()
    return render(request, 'posts/post_create.html',{'form':form})



class PostList(ListView):
    queryset = Post.objects.all()
    template_name= "posts/post_list.html"
    context_object_name= 'posts'



class PostDetail(DetailView):
    model =Post
    template_name= 'posts/post_detail.html'
    # context_object_name = 'posts'
    # def get_queryset(self):
        # return get_object_or_404(Post, pk=self.request.POST['pk'])
    def get_context_data(self,**kwargs):
        context = super(PostDetail,self).get_context_data()
        context['comments']=Comment.objects.filter(post=kwargs['object'].pk)
        return context



@api_view(['POST','GET'])
def index(request):
    # pk = request.query_params.get('pk')
    # print(request.query_params)
    pk = request.data.get('pk')
    try:
        p = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response({'detail': 'Post not exits'}, status=status.HTTP_404_NOT_FOUND)
    
    serialier = PostSerializer(p)
    return Response(serialier.data)