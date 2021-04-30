from django.urls import path
from FIRSTAPPLICATION import views

urlpatterns = [
    path('',views.index, name='home'),
    path('users/', views.userInfo, name="user_details"),
]