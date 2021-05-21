from django.urls import path
from tweets.views import tweet_view

urlpatterns = [
    path('', tweet_view, name='homepage'),
]
