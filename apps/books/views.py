# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404
from lib.decorators import render_to
from datetime import datetime, timedelta
from books.models import Book

from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

@render_to('books.html')
#@login_required()
def books(request):
    out = {}

#    out['user']  = 'Книги для заочников группы %s' % request.user
    out['books'] = Book.objects.all().filter(group=request.user)

#    out['user']  = request.user
#    out['books'] = Book.objects.all().filter(group=request.user)


#    out['now']   = datetime.now().strftime("%d.%m.%y %H:%M")
#    out['stuff'] = Staff.objects.all()
#    out['news']  = News.objects.all().order_by("-id")[:3]
    return out