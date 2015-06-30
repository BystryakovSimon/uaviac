# -*- coding: utf-8 -*-
from django.contrib import admin
from graduation.models import Graduation, Group, Student

class StudentChoice(admin.StackedInline):
    model = Student
    extra = 10

class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'graduation',)
    list_filter  = ('graduation',)
    inlines = [StudentChoice]


admin.site.register(Group, GroupAdmin)
admin.site.register(Graduation)