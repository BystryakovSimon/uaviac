# -*- coding: utf-8 -*-
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from schedule.models import SchedulePartTime, ScheduleFullTime
from django.utils.translation import ugettext as _
from pytils import dt


class ScheduleFullTimePlugin(CMSPluginBase):
    name = _(u"Расписание для очного отделения")
    render_template = "schedule.html"

    def render(self, context, instance, placeholder):

        context.update({
            'schedule'      : ScheduleFullTime.objects.all().order_by("-id")[0],
            'schedule_date' : dt.ru_strftime(u"%d %B", ScheduleFullTime.objects.all().order_by("-id")[0].date, inflected=True),
            'object'        : instance,
            'placeholder'   : placeholder,
        })
        return context


class SchedulePartTimePlugin(CMSPluginBase):
    name = _(u"Расписание для заочного отделения")
    render_template = "schedule.html"

    def render(self, context, instance, placeholder):

        context.update({
            'schedule'    : SchedulePartTime.objects.all().order_by("-id")[0],
            'schedule_date' : dt.ru_strftime(u"%d %B", SchedulePartTime.objects.all().order_by("-id")[0].date, inflected=True),
            'object'      : instance,
            'placeholder' : placeholder,
        })
        return context

plugin_pool.register_plugin(ScheduleFullTimePlugin)
plugin_pool.register_plugin(SchedulePartTimePlugin)