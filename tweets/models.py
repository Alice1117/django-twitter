from django.db import models
from django.contrib.auth.models import User
from utils.time_helpers import utc_now

# Create your models here:.
class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def hours_to_now(self):
        return (utc_now() - self.created_at).seconds

    def __str__(self):
        #The below content will be displayed when execute print(tweet instance)
        return f'{self.created_at} {self.user}: {self.content}'