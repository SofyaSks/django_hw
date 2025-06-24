from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Article(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    text = models.CharField(max_length=100000)
    dt = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__ (self):
        return self.title
    
   
class Subscriptions(models.Model):
    follower = models.ForeignKey(User, default=None, related_name='follower', on_delete=models.CASCADE)
    following = models.ForeignKey(User, default=None, related_name='following', on_delete=models.CASCADE)
    


