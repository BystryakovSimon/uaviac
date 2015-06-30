# -*- coding: utf-8 -*-
from django.contrib import admin
from media.models import Albom, Image#, Video
from sorl.thumbnail.admin import AdminImageMixin


class ImageChoice(AdminImageMixin, admin.TabularInline):
    fieldsets = [
        ('Выберите изображение', {'fields': ['alt', 'img',],}),
    ]
    model = Image
    extra = 20

class AlbomAdmin(AdminImageMixin, admin.ModelAdmin):
    model = Albom
    fieldsets = [
        ('Информация о альбоме', {'fields': ['is_published','name', 'cover'],}),
        ('Изменить дату публикации' , {'fields': ['date'], 'classes': ['collapse']}),
        ]
    inlines = [ImageChoice]
    search_fields = ['name']
    list_display = ('name','id','date', 'is_published','cover_thumbs_preview')


class ImageAdmin(AdminImageMixin, admin.ModelAdmin):
    fieldsets = [
        ('Информация о картинке', {'fields': ['alt', 'img','albom'],}),
        ('Изменить дату публикации' , {'fields': ['date'], 'classes': ['collapse']}),
        ]
    list_display = ('alt','img_thumbs_preview')
#
#class VideoAdmin(AdminImageMixin, admin.ModelAdmin):
#    list_display = ('name','img_thumbs_preview')
#
#
#admin.site.register(Video, VideoAdmin)
admin.site.register(Albom, AlbomAdmin)
admin.site.register(Image, ImageAdmin)