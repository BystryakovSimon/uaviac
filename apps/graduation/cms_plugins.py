# -*- coding: utf-8 -*-
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from graduation.models import Graduation, GraduationPlugin as GraduationPluginModel
from django.utils.translation import ugettext as _


class GraduationPlugin(CMSPluginBase):
    name = _(u"Выпускники")
    render_template = "graduation.html"

    def render(self, context, instance, placeholder):

        context.update({
            'graduations' : Graduation.objects.all().order_by("-id"),
            'object'      : instance,
            'placeholder' : placeholder,
        })
        return context

plugin_pool.register_plugin(GraduationPlugin)