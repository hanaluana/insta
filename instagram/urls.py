"""instagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts import views as accounts_views
from posts import views as posts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
    path('accounts/', include('accounts.urls')),
    path('<str:username>/', accounts_views.people, name="people"),
    path('',posts_views.list, name="root"),
]

# Dev에서는 꼭 써야함. (Debug=True 일 때 꼭 있어야 됨. 만약 False이면 이 줄은 빈 리스트를 반환함)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) # 통과시키고자 하는 url, 실제 저장장소
