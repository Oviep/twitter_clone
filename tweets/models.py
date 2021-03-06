from django.db import models


# Create your models here.
class Tweet(models.Model):
    tweet_field = models.CharField(max_length=280)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tweet_field
