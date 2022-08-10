from django.shortcuts import render, reverse
from django.views import View
from django.views.generic.edit import UpdateView

from .models import Topic, SubTopic


class HomeTopics(View):
    """Home page class based view"""

    def get(self, request):
        """GET request for Home page"""
        template = 'django_basics/basics.html'

        topics = Topic.objects.all()  # pylint: disable=no-member  # noqa E501

        context = {
            'custom_topics_name': topics,
        }

        return render(request, template, context)


class TopicDetails(View):
    """Topic details class based view"""

    def get(self, request, *args, **kwargs):
        """Topic details GET request"""
        topic = Topic.objects.get(slug=kwargs['slug'])  # pylint: disable=no-member  # noqa E501
        subtopics = topic.sub_topics.all().order_by('order_no')
        template = 'django_basics/details.html'

        context = {
            'topic': topic,
            'subtopics': subtopics
        }

        return render(request, template, context)


class TopicUpdateView(UpdateView):
    """
    Allow update of Topic from frontend
    """
    model = Topic
    fields = [
        "subject",
        "description",
        "image",
        "order_no"
    ]

    def get_success_url(self) -> str:
        """
        Returns url to use if edit is successful
        """
        slug = self.object.topic.slug
        return reverse('topic_details', args=[slug])


class SubTopicUpdateView(UpdateView):
    """
    Allow update of SubTopic from frontend
    """
    model = SubTopic
    fields = [
        "heading",
        "paragraph",
        "image",
        "order_no"
    ]

    def get_success_url(self) -> str:
        """
        Returns url to use if edit is successful
        """
        slug = self.object.topic.slug
        return reverse('topic_details', args=[slug])
