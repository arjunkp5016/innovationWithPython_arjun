from django.urls import path,include
from BLOG_POSTS import views

app_name = 'BLOG_POSTS'

urlpatterns = [
    path('',views.index,name='index'),
    path('users/',views.listUsers, name='users'),
    path('add/',views.postUsers, name='adduser'),
    path('delete/<int:pk>',views.user_delete, name='deluser'),
    path('about/',views.About, name = 'about'),
]
