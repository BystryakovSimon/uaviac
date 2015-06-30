# -*- coding: utf-8 -*-
from django.db import models
from cms.models import CMSPlugin
from datetime import datetime, timedelta
from ckeditor.fields import RichTextField


class ScheduleFullTime(models.Model):
    date          = models.DateTimeField(u'Дата расписания', default=datetime.now()+timedelta(days=1))
    schedule_list = RichTextField(u'Расписание(без даты)')

    class Meta:
        verbose_name        = u'Расписание очного отделения'
        verbose_name_plural = u'Список расписаний очного отделения'
        ordering            = ['id']
        get_latest_by       = "-id"

    def __unicode__(self):
        return u"%s" % self.date.strftime("%d.%m.%y")


class SchedulePartTime(models.Model):
    date          = models.DateTimeField(u'Дата расписания', default=datetime.now()+timedelta(days=1))
    schedule_list = RichTextField(u'Расписание(без даты)')

    class Meta:
        verbose_name        = u'Расписание заочного отделения'
        verbose_name_plural = u'Список расписаний заочного отделения'
        ordering            = ['id']
        get_latest_by       = "-id"

    def __unicode__(self):
        return u"%s" % self.date.strftime("%d.%m.%y")


class ScheduleFullTimePlugin(CMSPlugin):
    schedulefulltime = models.ForeignKey(ScheduleFullTime)


class SchedulePartTimePlugin(CMSPlugin):
    scheduleparttime = models.ForeignKey(SchedulePartTime)

