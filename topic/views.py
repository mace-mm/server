from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets
from .serializers import TopicSerializer
from .models import Topic 

class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all().order_by('-name')
    serializer_class = TopicSerializer


