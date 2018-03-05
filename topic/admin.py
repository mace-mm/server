from django.contrib import admin
from .models import Topic, Meeting, Objective, Decision, Action

# Register your models here.
admin.site.register(Topic)
admin.site.register(Meeting)
admin.site.register(Objective)
admin.site.register(Decision)
admin.site.register(Action)
