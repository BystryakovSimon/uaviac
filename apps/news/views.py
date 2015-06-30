# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404
from lib.decorators import render_to
from datetime import datetime, timedelta
from news.models import News

@render_to('news.html')
def news(request):
	out = {}
	out['all_news']  = News.published.all()
	return out

@render_to('news_id.html')
def news_id(request, news_id):
	out = {}
	out['news']       = News.published.filter(id=news_id)[0]
#	out['news']       = get_object_or_404(News, pk=news_id)
	return out