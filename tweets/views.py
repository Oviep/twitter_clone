from django.shortcuts import render

# Create your views here.
from tweets.models import Tweet


def tweet_view(request):
    tweet_content = Tweet.objects.all()
    context = {
        "tweet_content": tweet_content
    }
    return render(request, "index.html", context)
