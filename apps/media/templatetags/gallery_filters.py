# -*- coding: utf-8 -*-
from django import template
from media.models import Albom, Image

register = template.Library()


@register.filter(name='get_images')
def get_images(albom):
    return albom.get_images.all()
