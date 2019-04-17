from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path('login/', views.login, name="login"),
    path('logout/',views.logout, name="logout"),
    path('register/', views.register, name="register"),
    path('update/', views.update, name="update"),
    path('delete/', views.delete, name="delete"),
    path('password/', views.password, name="password"),
    path('<int:user_id>/follow/', views.follow, name="follow"),
    path('<int:user_id>/followers', views.followers, name="followers"),
    path('<int:user_id>/followings', views.followings, name="followings"),
]