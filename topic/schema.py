import graphene
from graphene_django.types import DjangoObjectType
from topic.models import Topic, Meeting, Action


class MeetingType(DjangoObjectType):
    class Meta:
        model = Meeting


class TopicType(DjangoObjectType):
    class Meta:
        model = Topic


class Query(object):
    all_topics = graphene.List(TopicType)
    topic = graphene.Field(TopicType, id=graphene.Int(),
                           name=graphene.String())

    def resolve_all_topics(self, info, **kwargs):
        return Topic.objects.all()

    def resolve_topic(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Topic.objects.get(pk=id)

        if name is not None:
            return Topic.objects.get(name=name)

        return None
