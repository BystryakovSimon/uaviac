# -*- coding: utf-8 -*-
from django.contrib import admin
from specialties.models import Specialty
from sorl.thumbnail.admin import AdminImageMixin


class SpecialtyAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ('cipher', 'name', 'is_published', 'cover_preview')

admin.site.register(Specialty, SpecialtyAdmin)