# -*- coding: utf-8 -*-
from django import template

register = template.Library()


@register.filter(name='get_staff')
def get_staff(staff_group):
    return staff_group.get_staff.all()
