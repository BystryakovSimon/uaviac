# -*- coding: utf-8 -*-
from django.contrib import admin
from schedule.models import SchedulePartTime, ScheduleFullTime


class ScheduleFullTimeAdmin(admin.ModelAdmin):
    search_fields = ['date']

class SchedulePartTimeAdmin(admin.ModelAdmin):
    search_fields = ['date']

	
admin.site.register(ScheduleFullTime, ScheduleFullTimeAdmin)
admin.site.register(SchedulePartTime, SchedulePartTimeAdmin)