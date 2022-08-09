from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeTopics.as_view(), name='django_basics'),
    path('details/<slug:slug>', views.TopicDetails.as_view(), name='topic_details'),
    path('update_topic/<int:pk>/<slug:slug>', views.SubTopicUpdateView.as_view(), name='edit_subtopic')
]
