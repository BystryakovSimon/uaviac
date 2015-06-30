# -*- coding: utf-8 -*-
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class BookApp(CMSApp):
    name = _(u"Книги для заочников")
    urls = ["books.urls"] 

apphook_pool.register(BookApp)