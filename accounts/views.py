from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from .forms import CustomUserChangeForm, ProfileForm
from .models import Profile

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
            print(request.GET.get('next'))
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
            Profile.objects.create(user=user)
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

# 회원 정보 변경 action (편집 & 반영)
@login_required
def update(request):
    if request.method == "POST":
        user_change_form = CustomUserChangeForm(data = request.POST, instance=request.user.profile)
        profile_form = ProfileForm(data = request.POST, instance = request.user.profile)
        
        if user_change_form.is_valid() and profile_form.is_valid():
            user_change_form.save() # save()는 그 객체를 반환한다.
            profile_form.save()
        return redirect('people', request.user.username)
    else:
        user_change_form = CustomUserChangeForm(instance=request.user)
        
        profile, created = Profile.objects.get_or_create(user=request.user)
        profile_form = ProfileForm(instance=profile)
        context = {
            'user_change_form': user_change_form,
            'profile_form': profile_form,
        }
        return render(request, 'accounts/update.html', context)

def delete(request):
    if request.method == "POST":
        request.user.delete()
        return redirect('posts:list')
    return render(request, 'accounts/delete.html')

@login_required
def password(request):
    if request.method == "POST":
        password_change_form = PasswordChangeForm(request.user, request.POST)
        if password_change_form.is_valid():
            user = password_change_form.save()
            update_session_auth_hash(request, user)
        return redirect('people', user.username)
    else:
        password_change_form = PasswordChangeForm(request.user)
        context = {
            'password_change_form': password_change_form
        }
        return render(request, 'accounts/password.html', context)