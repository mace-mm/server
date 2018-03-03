from .models import Topic, Meeting, Decision
from rest_framework import serializers

class TopicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Topic
        fields = "__all__"