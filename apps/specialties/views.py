# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404
from lib.decorators import render_to
from specialties.models import Specialty


@render_to('specialty_cipher.html')
def specialty(request):
    out = {}
    out['specialty']   = Specialty.published.all()[0]
    out['specialties'] = Specialty.published.all()
    return out

@render_to('specialty_cipher.html')
def specialty_cipher(request, cipher):
    out = {}
    out['specialty']   = Specialty.published.filter(cipher=cipher)[0]
    out['specialties'] = Specialty.published.all()
    return out