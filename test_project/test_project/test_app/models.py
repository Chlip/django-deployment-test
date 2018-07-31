from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    portfolio = models.URLField(blank=True)

    

    def __str__(self):
        return self.user.username
    
class UserPost(models.Model):
    cos = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    topic = models.CharField(max_length=28,)
    text = models.TextField()
    def __str__(self):
        return '{}'.format(self.topic)