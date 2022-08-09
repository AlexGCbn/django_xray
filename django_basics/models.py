from django.db import models
from django.template.defaultfilters import slugify


class Topic(models.Model):
    """Topic model to display relevant topics"""

    subject = models.CharField(max_length=50, null=False, blank=False)
    slug = models.SlugField(max_length=50, null=False, blank=False)
    description = models.TextField(max_length=10000, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    order_no = models.IntegerField(default=0)

    class Meta:
        ordering = ['order_no']

    def __str__(self):
        return f'{self.subject}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.subject)
        if not self.order_no:
            count = len(Topic.objects.all())
            self.order_no = count + 1
        return super().save(*args, **kwargs)


class SubTopic(models.Model):
    """Add sub topics with content to Topic model"""

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="sub_topics")  # noqa E501
    heading = models.CharField(max_length=75, null=True, blank=True)
    paragraph = models.TextField(max_length=3000, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, default='placeholder')
    order_no = models.IntegerField(default=0)

    class Meta:
        ordering = ['order_no']

    def __str__(self):
        return f'{self.heading}'

    def save(self, *args, **kwargs):
        """Add order_no if not specifically defined"""
        if not self.order_no:
            subtopics = SubTopic.objects.filter(topic=self.topic)
            count = len(subtopics)
            self.order_no = count + 1
        return super().save(*args, **kwargs)
