# -*- coding: utf-8 -*-
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class SpecialtyApp(CMSApp):
    name = _(u"Специальности")
    urls = ["specialties.urls"]

apphook_pool.register(SpecialtyApp)