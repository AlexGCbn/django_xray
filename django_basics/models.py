from django.db import models


class Topic(models.Model):
    """Topic model to display relevant topics"""

    subject = models.CharField(max_length=50, null=False, blank=False)
    slug = models.SlugField(max_length=50, null=False, blank=False)
    description = models.TextField(max_length=10000, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f'A topic about: {self.subject}'
