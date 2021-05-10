from django.db import models

# Create your models here.

class blogUsers(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=200,unique=True)

    def __str__(self):
        return self.author
