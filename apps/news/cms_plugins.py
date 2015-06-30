# -*- coding: utf-8 -*-
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from news.models import News, NewsPlugin as NewsPluginModel
from django.utils.translation import ugettext as _


class NewsPlugin(CMSPluginBase):
    name = _(u"Последние новости")
    render_template = "last_news.html"

    def render(self, context, instance, placeholder):

        context.update({
            'last_news'   : News.published.all()[:3],
            'object'      : instance,
            'placeholder' : placeholder,
        })
        return context

plugin_pool.register_plugin(NewsPlugin)