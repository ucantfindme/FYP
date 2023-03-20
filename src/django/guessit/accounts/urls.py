from django.urls import path
from .views import register,home,login_view,logout_view,play,profile

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/',profile,name='profile'),
    path('play/',play,name='play'),
    path('', home, name='home'),
]