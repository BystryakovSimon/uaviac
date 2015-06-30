# -*- coding: utf-8 -*-
from django.contrib import admin
from books.models import Book

class BookAdmin(admin.ModelAdmin):
	list_display = ('name', 'group',)
	list_filter  = ('group',)

admin.site.register(Book, BookAdmin)