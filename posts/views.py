from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post
from django.views.decorators.http import require_POST


# Create your views here.

def create(request):
    if request.method=="POST":
        # 작성된 post를 DB에 적용
        form =PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('posts:list')
    else:
        # 새로 post 작성하는 form 페이지 보여줌
        form = PostForm()
        return render(request, 'posts/create.html', {'form':form})
        
def list(request):
    posts = Post.objects.all()
    return render(request, 'posts/list.html', {'posts':posts})

@require_POST
def delete(request,post_id):
    post = Post.objects.get(pk=post_id)
    if post.user != request.user:
        return redirect('posts:list')
    post.delete()
    return redirect('posts:list')

def update(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if post.user != request.user:
        return redirect('posts:list')
    if request.method=="POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
        return redirect('posts:list')
    else:
        form = PostForm(instance = post)
        return render(request, 'posts/update.html', {'form':form})
        
def like(request,post_id):
    # 이 유저는 어떤 유저인가는 여기서 해결해준다.
    post = get_object_or_404(Post, pk= post_id)
    
    # 만약 user가 접속이 되어 있고, 클릭을 할때마다 현재 like의 상태를 반대로 바꿔준다.
    
    # 1. 만약, user가 해당 포스트를 이미 like 했다면, like를 해재한다.
    # 2. 아니면, like를 추가한다.
    if request.user in post.like_users.all():
        post.like_users.remove(request.user)
    else:
        post.like_users.add(request.user)
        
    return redirect('posts:list')
    