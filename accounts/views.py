from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
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
            form.save()
            auth_login(request, form.instance)
            # messages.success(request, '환영합니다! '+form.instance.username+'님')
            return redirect('posts:list')
        else:
            # messages.success(request, '회원가입에 실패하였습니다')
            return redirect('account:register')
    else:
        form = UserCreationForm()
        return render(request, 'accounts/register.html', {'form':form})