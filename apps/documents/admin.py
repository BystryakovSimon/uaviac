# -*- coding: utf-8 -*-
from django.contrib import admin
from documents.models import LocalAct, License, Budget, StudPosition
from sorl.thumbnail.admin import AdminImageMixin

class LocalActAdmin(AdminImageMixin, admin.ModelAdmin):
	list_display = ('name', 'is_published','img_thumbs_preview',)

class LicenseAdmin(AdminImageMixin, admin.ModelAdmin):
	list_display = ('name', 'is_published', 'img_thumbs_preview',)

class BudgetAdmin(AdminImageMixin, admin.ModelAdmin):
	list_display = ('name', 'is_published', 'img_thumbs_preview',)

class StudPositionAdmin(AdminImageMixin, admin.ModelAdmin):
	list_display = ('name', 'is_published', 'img_thumbs_preview',)

admin.site.register(StudPosition, StudPositionAdmin)
admin.site.register(Budget, BudgetAdmin)
admin.site.register(License, LicenseAdmin)
admin.site.register(LocalAct, LocalActAdmin)