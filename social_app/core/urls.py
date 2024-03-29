from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    path('settings', views.settings, name='settings'),
    path('search', views.search, name='search'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('send_friend_request/<str:pk>', views.send_friend_request, name='send_friend_request'),
    path('accept_friend_request/<int:requestId>', views.accept_friend_request, name='accept_friend_request'),
]