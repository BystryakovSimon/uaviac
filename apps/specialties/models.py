# -*- coding: utf-8 -*-
from django.db import models
from cms.models import CMSPlugin
from datetime import datetime
from sorl.thumbnail import ImageField, get_thumbnail
from ckeditor.fields import RichTextField


class SpecialtyManager(models.Manager):
    def get_query_set(self):
        return super(SpecialtyManager, self).get_query_set().filter(is_published=True)

class Specialty(models.Model):
    is_published = models.BooleanField(u'Опубликована', default=True)
    cipher       = models.IntegerField(u'Шифр специальности')
    name         = models.CharField(u'Название специальности', max_length=200)
    cover        = ImageField(u'Выберите картинку',  upload_to=u"images/specialty_covers", blank=True)
    text         = RichTextField(u'Квалификационная характеристика выпускника')

    objects      = models.Manager()
    published    = SpecialtyManager()

    def cover_preview(self):
        if self.cover:
            return u'<img src="%s"  width="75" height="75" >' %  get_thumbnail(self.cover, '75x75', crop='center', quality=99).url
        else:
            return '(none)'
    cover_preview.short_description = u'Миниатюра'
    cover_preview.allow_tags        = True

    class Meta:
        verbose_name        = u'Специальность'
        verbose_name_plural = u'Специальности'
        ordering            = ['id']
        get_latest_by       = "-id"

    def __unicode__(self):
        return self.name

class SpecialtyPlugin(CMSPlugin):
    name = models.ForeignKey(Specialty)