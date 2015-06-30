# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404
from lib.decorators import render_to
from schedule.models import Schedule
#from schedule.forms  import ScheduleForm

@render_to('schedule.html')
def schedule(request):
    out = {}

#    out['calendar'] = ScheduleForm(request.POST)

#    if 'calendar' in request.POST and request.POST['calendar']:
#        out['schedule'] = Schedule.objects.filter(id=request.POST['calendar'])[0]
#    else:
    out['schedule'] = Schedule.objects.all().order_by("-date")[0]
    return out
 