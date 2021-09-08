from django.db import models

# Create your models here.
class Tweet(models.Model):
    excerpt = models.CharField(max_length=300)
    date = models.DateTimeField('date published')

# Figure out how to add index table with rel to Tweet table
# Will need to update db (makemigrations??)

# class Position(models.Model):
#     tweet = models.ForeignKey(Tweet, )
#     index = models.IntegerField(default=0)