from django.shortcuts import render
from FIRSTAPPLICATION.models import Info

# Create your views here.
def index(request):
    return render(request, 'First_application/demo.html')


def userInfo(request):
    user_list = Info.objects.order_by('Name')
    return render(request, 'First_application/users.html', context={'user':user_list})