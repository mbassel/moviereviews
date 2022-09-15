from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render
from .models import News
# Create your views here.


def news(request):
    news = News.objects.all().order_by('-date')
    context = {
        'news':  news,
    }
    return render(request, 'news.html', context)
