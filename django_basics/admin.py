from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Topic


@admin.register(Topic)
class TopicAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('subject',)}
    list_display = ('subject', 'description')
    summernote_fields = ('description')