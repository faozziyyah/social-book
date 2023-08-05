from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin, name='signin'),
    path('index', views.index, name='index'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('settings', views.settings, name='settings'),
    path('upload', views.upload, name='upload'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('follow', views.follow, name='follow'),
    path('search', views.search, name='search'),
    #path('show-post/<id>', views.show_post, name='show-post'),
    #path('show-post/<str:id>/comment', views.add_comment, name='add-comment'),
    path('like-post', views.like_post, name='like-post'),
]