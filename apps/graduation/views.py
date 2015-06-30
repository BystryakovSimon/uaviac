# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404
from lib.decorators import render_to
from graduation.models import Graduation


@render_to('graduation_year.html')
def graduation(request):
    out = {}
    out['graduation']  = Graduation.objects.all().order_by("-year")[0]
    out['graduations'] = Graduation.objects.all().order_by("-year")
    return out

@render_to('graduation_year.html')
def graduation_year(request, year):
    out = {}
    out['graduation']  = get_object_or_404(Graduation, year=year)
#    out['graduation']  = Graduation.objects.filter(year=year).order_by("-year")[0]
    out['graduations'] = Graduation.objects.all().order_by("-year")
    return out