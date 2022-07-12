from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Topic, SubTopic


@admin.register(Topic)
class TopicAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('subject',)}
    list_display = ('subject', 'description')
    summernote_fields = ('description')


@admin.register(SubTopic)
class SubTopicAdmin(SummernoteModelAdmin):
    list_display = ('topic', 'heading', 'paragraph', 'image')
    summernote_fields = ('paragraph')
