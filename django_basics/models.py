from django.db import models


class Topic(models.Model):
    """Topic model to display relevant topics"""

    subject = models.CharField(max_length=50, null=False, blank=False)
    slug = models.SlugField(max_length=50, null=False, blank=False)
    description = models.TextField(max_length=10000, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f'{self.subject}'

class SubTopic(models.Model):
    """Add sub topics with content to Topic model"""

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="sub_topics")  # noqa E501
    heading = models.CharField(max_length=75, null=True, blank=True)
    paragraph = models.TextField(max_length=2000, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, default='placeholder')

    def __str__(self):
        return f'{self.heading}'
