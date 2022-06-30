from django.shortcuts import render
from django.views import View
from .models import Topic


class HomeTopics(View):
    """Home page class based view"""

    def get(self, request):
        """GET request for Home page"""
        template = 'skeleton/home.html'

        topics = Topic.objects.all()

        context = {
            'custom_topics_name': topics,
        }

        return render(request, template, context)
