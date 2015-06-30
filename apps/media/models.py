# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from cms.models import CMSPlugin
from sorl.thumbnail import ImageField, get_thumbnail


def get_cover_path_for_albom(instance, filename):
#    return u"images/alboms/%s/cover/%s" % (str(instance.date.strftime("%d-%m-%Y_%H-%M-%S")), filename)
    return u"images/alboms/%s/cover/%s" % (str(instance.id), filename)

#def get_archive_path_for_albom(instance, filename):
#    return u"images/alboms/%s/archive/%s" % (str(instance.date.strftime("%d-%m-%Y_%H-%M-%S")), filename)

class AlbomManager(models.Manager):
    def get_query_set(self):
        return super(AlbomManager, self).get_query_set().filter(is_published=True)

class Albom(models.Model):
    is_published = models.BooleanField(u'Опубликована', default=True)
    date         = models.DateTimeField(u'Дата публикации', default=datetime.now())
    name         = models.CharField(u'Название альбома', max_length=100)
    cover        = ImageField(u"Выберите обложку", upload_to=get_cover_path_for_albom)
#    archive      = models.FileField('Выберите архив альбома для скачивания', blank=True, upload_to=get_archive_path_for_albom)
    
    objects      = models.Manager()
    published    = AlbomManager()

    def cover_thumbs_preview(self):
        if self.cover:
            return u'<img src="%s" width="75" height="75" >' % get_thumbnail(self.cover, '75x75', crop='center', quality=99).url
        else:
            return '(none)'
    cover_thumbs_preview.short_description = u'Обложка'
    cover_thumbs_preview.allow_tags        = True

    class Meta:
        verbose_name        = u'Альбом'
        verbose_name_plural = u'Альбомы'
        ordering            = ['-id']
        get_latest_by       = "-id"

    def __unicode__(self):
        return u'%s' % self.name


class AlbomPlugin(CMSPlugin):
    albom = models.ForeignKey(Albom)


def get_path_for_img(instance, filename):
#    return u"images/alboms/%s/imgs/%s" % (str(instance.albom.date.strftime("%d-%m-%Y_%H-%M-%S")), filename)
    return u"images/alboms/%s/imgs/%s" % (str(instance.albom.id), filename)

class Image(models.Model):
    alt        = models.CharField(u'Название', max_length=50, blank=True)
    img        = ImageField(u"Выберите изображение", upload_to=get_path_for_img)
    date       = models.DateTimeField(u'Дата публикации', default=datetime.now())
    albom      = models.ForeignKey(Albom, verbose_name="Альбом", related_name="get_images", null=True, blank=True)

    def img_thumbs_preview(self):
        if self.img:
            return u'<img src="%s" width="75" height="75"  >' % get_thumbnail(self.img, '75x75', crop='center', quality=99).url
        else:
            return '(none)'
    img_thumbs_preview.short_description = u'Обложка'
    img_thumbs_preview.allow_tags        = True


    class Meta:
        verbose_name        = u'Изображение'
        verbose_name_plural = u'Изображения'
        ordering            = ['id']
        get_latest_by       = "-id"

    def __unicode__(self):
        return '%s %s' % (self.alt, self.img)

#class Video(models.Model):
#    name  = models.CharField('Навзание видео', max_length=100)
#    image = models.FileField('Выберите обложку видео',null=True, blank=True, upload_to='images/videos_covers/')
#    webm  = models.FileField('Видео в формате webm(chrome, opera, firefox)',null=True, blank=True, upload_to='videos/webm/')
#    ogg   = models.FileField('Видео в формате ogg(chrome, opera, firefox)',null=True, blank=True, upload_to='videos/ogg/')
#    mp4   = models.FileField('Видео в формате mp4(ie, chrome, safari)',null=True, blank=True, upload_to='videos/mp4/')
#
#    def img_thumbs_preview(self):
#        if self.image:
#            return u'<img src="%s" width="75" height="75"  >' % get_thumbnail(self.image, '75x75', crop='center', quality=99).url
#        else:
#            return '(none)'
#    img_thumbs_preview.short_description = u'Обложка'
#    img_thumbs_preview.allow_tags        = True
#
#    class Meta:
#        verbose_name        = 'Видео'
#        verbose_name_plural = 'Видео'
#        ordering            = ['id']
#        get_latest_by       = "-id"
#
#    def __unicode__(self):
#        return name
