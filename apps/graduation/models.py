# -*- coding: utf-8 -*-
from django.db import models
from cms.models import CMSPlugin
from media.models import Albom, Image


class Graduation(models.Model):
    year        = models.IntegerField('Год выпуска')
    albom       = models.ForeignKey(Albom, verbose_name="Выпускной альбом", null=True, blank=True)
#    video       = models.ForeignKey(Video, verbose_name="Видео",  null=True, blank=True)

    class Meta:
        verbose_name        = u'Год выпуска'
        verbose_name_plural = u'Года выпуска'
        ordering            = ['id']
        get_latest_by       = "-id"

    def __unicode__(self):
        return u'%s' %self.year


class Group(models.Model):
    graduation    = models.ForeignKey(Graduation, verbose_name=u"Выпуск", related_name="get_groups")
    name          = models.CharField(u'Группа', max_length=100)
    specialty     = models.CharField(u'Специальность', max_length=200)
    form_master   = models.CharField(u'Классный руководитель', max_length=100)
    albom         = models.ForeignKey(Albom, verbose_name="Выпускной альбом", null=True, blank=True)
#    video         = models.ForeignKey(Video, verbose_name="Видео",  null=True, blank=True)

    class Meta:
        verbose_name        = u'Выпустившаяся группы'
        verbose_name_plural = u'Выпустившиеся группы'
        ordering            = ['id']
        get_latest_by       = "-id"

    def __unicode__(self):
        return u'%s' % self.name


class Student(models.Model):
    fio   = models.CharField(u'Фамилия Имя Отчество', max_length=100) 
    img   = models.ForeignKey(Image, verbose_name="Фото студента", null=True, blank=True)
    group = models.ForeignKey(Group, verbose_name="Группа", related_name="get_students")


    class Meta:
        verbose_name        = u'Выпускник'
        verbose_name_plural = u'Выпускники'
        ordering            = ['id']
        get_latest_by       = "-id"

    def __unicode__(self):
        return u'%s' % (self.fio)



#class GraduationPlugin(CMSPlugin):
#    staff = models.ForeignKey('vipyskniki.Graduation', related_name='plugins')

#    def __unicode__(self):
#        return self.vipyskniki.year
