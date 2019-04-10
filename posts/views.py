from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post

# Create your views here.

def create(request):
    if request.method=="POST":
        # 작성된 post를 DB에 적용
        form =PostForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('posts:create')
    else:
        # 새로 post 작성하는 form 페이지 보여줌
        form = PostForm()
        return render(request, 'posts/create.html', {'form':form})
        
def index(request):
    posts = Post.objects.all()
    return render(request, 'posts/list.html', {'posts':posts})
        