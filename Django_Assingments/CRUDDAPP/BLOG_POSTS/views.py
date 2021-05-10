from django.shortcuts import render, redirect, get_object_or_404,reverse
from BLOG_POSTS.forms import NewUserForm
from BLOG_POSTS.models import blogUsers



# Create your views here.
def index(request):
    return render(request, 'BLOG_POSTS/index.html')

def About(request):
    return render(request, 'BLOG_POSTS/aboutus.html')


#view for GET METHOD
def listUsers(request,template_name= 'BLOG_POSTS/POST_LIST.html'):
    people = blogUsers.objects.all()
    return render(request,template_name,context={'users':people})

#view for POST METHOD
def postUsers(request, template_name= 'BLOG_POSTS/POST_FORM.html'):

    form = NewUserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/users')
    return render(request,template_name, context={'form':form})


#view for deleting record from database
def user_delete(request, pk, template_name='BLOG_POSTS/POST_DELETE.html'):
    user = get_object_or_404(blogUsers, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('/users')
    return render(request,template_name, {'object':user})
