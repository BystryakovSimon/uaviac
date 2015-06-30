# -*- coding: utf-8 -*-
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from media.models import Albom
from django.utils.translation import ugettext as _

class AlbomPlugin(CMSPluginBase):
    name = _(u"Последние альбомы")
    render_template = "gallery_main.html"

    def render(self, context, instance, placeholder):

        context.update({
			'alboms'      : Albom.published.all().order_by("-id")[:16],
			'alboms_list' : Albom.published.all().order_by("-id")[:8],
            'object'      : instance,
            'placeholder' : placeholder,
        })
        return context

plugin_pool.register_plugin(AlbomPlugin)