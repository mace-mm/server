from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets
from .serializers import TopicSerializer, MeetingSerializer, ObjectiveSerializer, DecisionSerializer, ActionSerializer
from .models import Topic, Meeting, Objective, Decision, Action


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all().order_by('-name')
    serializer_class = TopicSerializer


class MeetingViewSet(viewsets.ModelViewSet):
    queryset = Meeting.objects.all().order_by('-date')
    serializer_class = MeetingSerializer


class ObjectiveViewSet(viewsets.ModelViewSet):
    queryset = Objective.objects.all()
    serializer_class = ObjectiveSerializer


class DecisionViewSet(viewsets.ModelViewSet):
    queryset = Decision.objects.all()
    serializer_class = DecisionSerializer


class ActionViewSet(viewsets.ModelViewSet):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer
