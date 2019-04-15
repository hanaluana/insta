from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
# users/login 에 들어왔을 때
def login(request):
    if request.method=="GET":
        # 로그인 정보 입력
        form = AuthenticationForm()
    else:
        # 로그인을 시키고 (User를 인증하고)
        form = AuthenticationForm(request, request.POST)
        
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'posts:list') # next=가 정의 되어 있으면, 해당하는 url로, 아니면 list로...
        else:
            return redirect('accounts:login')
            # 로그인이 안됬다고 알려준다.
    return render(request, 'accounts/login.html', {'form':form})
        
def logout(request):
    # 세션에서 유저를 지운다.
    auth_logout(request)
    return redirect('posts:list')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('posts:list')
        else:
            return redirect('account:register')
    else:
        form = UserCreationForm()
        return render(request, 'accounts/register.html', {'form':form})
        
def people(request, username):
    people = get_object_or_404(get_user_model(), username=username) # 모델, username=""
    # 1. settings.AUTH_USER_MODEL (django.conf에 있음)
    # 2. get_user_model() : 얘는 아예 객체를 return
    # 3. User (django.contrib.auth.models에 있는 친구) : 얘는 쓰면 안 좋음
    return render(request, 'accounts/people.html', {'people': people })
