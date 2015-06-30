# -*- coding: utf-8 -*-
from django import forms
from models import Schedule
from django.contrib.admin import widgets                                       
from widgets import JqSplitDateTimeWidget
from fields import JqSplitDateTimeField

class ScheduleForm(forms.ModelForm):
    calendar = JqSplitDateTimeField(widget=JqSplitDateTimeWidget(attrs={'date_class':'datepicker','time_class':'timepicker'})