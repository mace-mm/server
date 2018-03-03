from django.db import models
from django.contrib.auth.models import User

class TopicStatus(models.Model):
    name = models.CharField(max_length=20, unique=True)   
    topic_statuses = models.Manager()

class Topic(models.Model):
    name = models.CharField(max_length=20, unique=True)    
    description = models.TextField()
    status = models.ForeignKey(TopicStatus, on_delete=models.CASCADE)

class Meeting(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    date = models.DateTimeField()
    
    class Meta:
        unique_together = ('topic', 'date')

class Decision(models.Model):
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    text = models.TextField()

class Action(models.Model):
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    text = models.TextField()
    complete = models.BooleanField
    owner = models.ForeignKey(User)

