from django.db import models

# Create your models here.
class Tweet(models.Model):
    excerpt = models.CharField(max_length=300)
    date = models.DateTimeField('date published')

class Position(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    index = models.IntegerField(default=0)