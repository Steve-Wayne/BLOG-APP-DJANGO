from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    # we are going to create the same attributes that we previously defined 
    title=models.CharField(max_length=1000)
    content=models.TextField()
    date_posted=models.DateTimeField(default= timezone.now)
    #here now does not have () behind it as it is usually for a function
    #it is because we dont actually want to execute that function right now
    # we just want to pass that function as a default value
    authors=models.ForeignKey(User , on_delete=models.CASCADE)
    # on_delete=models.CASCADE on deleting the user it delets all related content to it
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail' , kwargs={'pk': self.pk })
    

    