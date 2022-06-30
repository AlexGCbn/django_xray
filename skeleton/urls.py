from django.urls import path

urlpatterns = [
    path('', views.HomeTopics.as_view(), name='home'),
]
