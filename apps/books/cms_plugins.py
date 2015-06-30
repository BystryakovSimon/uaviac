# -*- coding: utf-8 -*-
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from books.models import BookPlugin as BookPluginModel
from django.utils.translation import ugettext as _

class BookPlugin(CMSPluginBase):
    model = BookPluginModel
    name = _(u"Заочники")
    render_template = "books.html"

    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context


plugin_pool.register_plugin(BookPlugin)