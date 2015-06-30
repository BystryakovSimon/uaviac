# -*- coding: utf-8 -*-
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from specialties.models import Specialty, SpecialtyPlugin
from django.utils.translation import ugettext as _


class SpecialtyPlugin(CMSPluginBase):
    name = _(u"Специальности")
    render_template = "specialties.html"

    def render(self, context, instance, placeholder):

        context.update({
            'specialties' : Specialty.published.all(),
            'object'      : instance,
            'placeholder' : placeholder,
        })
        return context

plugin_pool.register_plugin(SpecialtyPlugin)