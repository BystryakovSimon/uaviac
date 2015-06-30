# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404
from lib.decorators import render_to
from datetime import datetime, timedelta
from media.models import Albom


@render_to('gallery.html')
def gallery(request):
	out = {}
	out['all_alboms'] = Albom.published.all()#.order_by("id")
	return out

@render_to('3DWallGallery.html')
def gallery_id(request, gallery_id):
	out = {}
#	out['albom'] = get_object_or_404(Albom, id=gallery_id)
	out['albom'] = Albom.published.filter(id=gallery_id)[0]
	return out