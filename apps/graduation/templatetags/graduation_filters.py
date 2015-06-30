# -*- coding: utf-8 -*-
from django import template
register = template.Library()

@register.filter(name='groups')
def groups(graduation):
    return graduation.get_groups.all()

@register.filter(name='students')
def students(group):
    return group.get_students.all().order_by("fio")
