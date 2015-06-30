# -*- coding: utf-8 -*-
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from documents.models import  LocalAct, License, Budget, StudPosition
from django.utils.translation import ugettext as _

class LocalActPlugin(CMSPluginBase):
    name = _(u"Локальные акты")
    render_template = "localacts.html"

    def render(self, context, instance, placeholder):

        context.update({
			'localacts'   : LocalAct.published.all(),
            'object'      : instance,
            'placeholder' : placeholder,
        })
        return context

class LicensePlugin(CMSPluginBase):
    name = _(u"Лицензии и свидетельства")
    render_template = "license.html"

    def render(self, context, instance, placeholder):

        context.update({
			'licenses'    : License.published.all(),
            'object'      : instance,
            'placeholder' : placeholder,
        })
        return context

class BudgetPlugin(CMSPluginBase):
    name = _(u"Бюджетная смета на год")
    render_template = "budget.html"

    def render(self, context, instance, placeholder):

        context.update({
			'documents'   : Budget.objects.all(),
            'object'      : instance,
            'placeholder' : placeholder,
        })
        return context

class StudPositionPlugin(CMSPluginBase):
    name = _(u"Положения для студентов")
    render_template = "studposition.html"

    def render(self, context, instance, placeholder):

        context.update({
            'documents'   : StudPosition.objects.all(),
            'object'      : instance,
            'placeholder' : placeholder,
        })
        return context

plugin_pool.register_plugin(StudPositionPlugin)
plugin_pool.register_plugin(BudgetPlugin)
plugin_pool.register_plugin(LicensePlugin)
plugin_pool.register_plugin(LocalActPlugin)