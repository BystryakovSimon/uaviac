# -*- coding: utf-8 -*-
from django.contrib import admin
from staff.models import Staff, StaffGroup
from sorl.thumbnail.admin import AdminImageMixin


class StaffGroupAdmin(admin.ModelAdmin):
    list_display = ('staffgroupname', 'order')


class StaffAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ('admin_show','photo_preview')
    list_filter  = ('staffgroup',)

admin.site.register(Staff, StaffAdmin)
admin.site.register(StaffGroup, StaffGroupAdmin)