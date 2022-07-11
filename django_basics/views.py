from django.shortcuts import render
from django.views import View
from .models import Topic


class HomeTopics(View):
    """Home page class based view"""

    def get(self, request):
        """GET request for Home page"""
        template = 'django_basics/basics.html'

        topics = Topic.objects.all()

        context = {
            'custom_topics_name': topics,
        }

        return render(request, template, context)


class TopicDetails(View):
    """Topic details class based view"""

    def get(self, request, *args, **kwargs):
        """Topic details GET request"""
        topic = Topic.objects.get(slug=kwargs['slug'])
        template = 'django_basic/details.html'

        context = {
            'topic': topic,
        }

        return render(request, template, context)
