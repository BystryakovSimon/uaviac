# -*- coding: utf-8 -*-
from django.contrib import admin
from news.models import News
from sorl.thumbnail.admin import AdminImageMixin


class NewsAdmin(AdminImageMixin, admin.ModelAdmin):
    fieldsets = [
        ('Изменить дату публикации', {'fields': ['date'],'classes': ['collapse']}),
        ('Добавление новости', {'fields': ['is_published', 'title', 'short', 'cover', 'albom', 'full'],}),
    ]
    search_fields = ['title']
    list_display = ('title', 'date', 'is_published', 'cover_preview')

admin.site.register(News, NewsAdmin)