from django.db import models
from django.conf import settings
from django.contrib.auth.models import User



class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['-timestamp']
