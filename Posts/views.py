from django.shortcuts import render
from Posts.models import Post,Comment
# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    context= {'posts':posts}
    return  render(request, 'posts/post_list.html', context= context)

def post_detail(request,pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    context= {'post':post, 'comment':comments}
    return render(request,'posts/post_detail.html',context=context)