from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeTopics.as_view(), name='home'),
    path('details/<slug:slug>', views.TopicDetails.as_view(), name='topic_details'),
]
