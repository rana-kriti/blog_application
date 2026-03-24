from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='root'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('home/', views.home, name='home'),
    path('newpost/', views.newpost, name='newpost'),
    path('myposts/', views.myposts, name='myposts'),
    path('signout/', views.signout, name='signout'),
]

