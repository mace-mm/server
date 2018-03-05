from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    archived = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Meeting(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    date = models.DateTimeField()

    class Meta:
        unique_together = ('topic', 'date')

    def __str__(self):
        return self.date.strftime('%b %-m %Y %-I:%M%p')


class Objective(models.Model):
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text


class Decision(models.Model):
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text


class Action(models.Model):
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    text = models.TextField()
    complete = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    due_date = models.DateField(null=True)

    def __str__(self):
        return self.text
