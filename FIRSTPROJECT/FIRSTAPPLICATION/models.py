from django.db import models

# Create your models here.
class Info(models.Model):
    Name = models.CharField(max_length=264)
    Contact = models.IntegerField(unique=True)
    Address = models.CharField(max_length=264)

    def __str__(self):
        return self.Name