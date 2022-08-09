from .models import Topic, SubTopic


def supply_topic_context(request):
    """Topics available on all templates"""

    topics = Topic.objects.all()
    topics_count = len(topics)

    context = {
        'topics_in_context': topics,
        'topics_count': topics_count
    }
    return context
