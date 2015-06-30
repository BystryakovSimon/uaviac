# -*- coding: utf-8 -*-
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from staff.models import StaffGroup, StaffPlugin as StaffPluginModel
from django.utils.translation import ugettext as _

class StaffPlugin(CMSPluginBase):
    name = _(u"Список сотрудников")
    render_template = "staff.html"

    def render(self, context, instance, placeholder):

        context.update({
            'staff_group' : StaffGroup.objects.all().order_by("order"),
            'object'      : instance,
            'placeholder' : placeholder,
        })
        return context

plugin_pool.register_plugin(StaffPlugin)