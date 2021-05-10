from django import forms
from BLOG_POSTS.models import blogUsers


class NewUserForm(forms.ModelForm):
    class Meta():
        model = blogUsers
        fields = '__all__'
