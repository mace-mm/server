from .models import Topic, Meeting, Objective, Decision, Action
from rest_framework import serializers


class TopicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Topic
        fields = "__all__"


class MeetingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Meeting
        fields = "__all__"


class ObjectiveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Objective
        fields = "__all__"


class DecisionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Decision
        fields = "__all__"


class ActionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Action
        fields = "__all__"
