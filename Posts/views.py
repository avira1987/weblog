from django.shortcuts import render
from Posts.models import Post,Comment
from Posts.forms import PostForm
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    context= {'posts':posts}
    return  render(request, 'posts/post_list.html', context= context)

def post_detail(request,pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    context= {'post':post, 'comments':comments}
    return render(request,'posts/post_detail.html',context=context)

def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            Post.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('posts/')
    else:
        form = PostForm()
    return render(request, 'posts/post_create.html',{'form':form})