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
]