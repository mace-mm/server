from django.contrib import admin
from .models import TopicStatus, Topic, Meeting, Decision

# Register your models here.
admin.site.register(TopicStatus)
admin.site.register(Topic)
admin.site.register(Meeting)
admin.site.register(Decision)
