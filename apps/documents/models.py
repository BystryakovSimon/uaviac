# -*- coding: utf-8 -*-
from django.db import models
from sorl.thumbnail import ImageField, get_thumbnail
from cms.models import CMSPlugin


class LocalActManager(models.Manager):
    def get_query_set(self):
        return super(LocalActManager, self).get_query_set().filter(is_published=True)

class LocalAct(models.Model):
    is_published = models.BooleanField(u'Опубликована', default=True)
    name    = models.CharField(u'Название акта', max_length=200)
    cover   = ImageField(u"Выберите изображение", upload_to=u"images/local_acts/covers/")
    act     = models.FileField(u'Выберите акт', blank=True, upload_to='local_acts/')

    objects      = models.Manager()
    published    = LocalActManager()

    def img_thumbs_preview(self):
        if self.cover:
            return u'<img src="%s" width="75" height="75"  >' % get_thumbnail(self.cover, '75x75', crop='center', quality=99).url
        else:
            return '(none)'
    img_thumbs_preview.short_description = u'Миниатюра'
    img_thumbs_preview.allow_tags        = True

    class Meta:
        verbose_name        = u'Локальный акт'
        verbose_name_plural = u'Локальные акты'
        ordering            = ['id']
        get_latest_by       = "-id"

    def __unicode__(self):
        return u'%s'%self.name


class LicenseManager(models.Manager):
    def get_query_set(self):
        return super(LicenseManager, self).get_query_set().filter(is_published=True)

class License(models.Model):
    is_published = models.BooleanField(u'Опубликована', default=True)
    name    = models.CharField(u'Введите название лицензии или свидетельства', max_length=200)
    license = ImageField(u"Выберите лицензию или свидетельство", upload_to=u"images/licenses/")

    objects      = models.Manager()
    published    = LicenseManager()

    def img_thumbs_preview(self):
        if self.license:
            return u'<img src="%s" width="75" height="75"  >' % get_thumbnail(self.license, '75x75', crop='center', quality=99).url
        else:
            return '(none)'
    img_thumbs_preview.short_description = u'Миниатюра'
    img_thumbs_preview.allow_tags        = True

    class Meta:
        verbose_name        = 'Лицензия'
        verbose_name_plural = 'Лицензии'
        ordering            = ['id']
        get_latest_by       = "-id"

    def __unicode__(self):
        return u'%s'%self.name

class BudgetManager(models.Manager):
    def get_query_set(self):
        return super(BudgetManager, self).get_query_set().filter(is_published=True)

class Budget(models.Model):
    is_published = models.BooleanField(u'Опубликована', default=True)
    name    = models.CharField(u'Введите название документа', max_length=200)
    budget  = ImageField(u"Выберите документ", upload_to=u"images/budget/")

    objects      = models.Manager()
    published    = BudgetManager()

    def img_thumbs_preview(self):
        if self.budget:
            return u'<img src="%s" width="75" height="75"  >' % get_thumbnail(self.budget, '75x75', crop='center', quality=99).url
        else:
            return '(none)'
    img_thumbs_preview.short_description = u'Миниатюра'
    img_thumbs_preview.allow_tags        = True

    class Meta:
        verbose_name        = 'Бюджетная смета на год'
        verbose_name_plural = 'Бюджетная смета на год'
        ordering            = ['id']
        get_latest_by       = "-id"

    def __unicode__(self):
        return u'%s'%self.name

class StudPositionManager(models.Manager):
    def get_query_set(self):
        return super(StudPositionManager, self).get_query_set().filter(is_published=True)

class StudPosition(models.Model):
    is_published   = models.BooleanField(u'Опубликована', default=True)
    name           = models.CharField(u'Введите название положения', max_length=200)
#    stud_position  = ImageField("Выберите документ", upload_to=u"images/stud_position/")
    cover          = ImageField(u"Выберите изображение", upload_to=u"images/stud_position/covers/")
    stud_position  = models.FileField(u"Выберите документ", upload_to=u"images/stud_position/")

    objects      = models.Manager()
    published    = StudPositionManager()

    def img_thumbs_preview(self):
        if self.stud_position:
            return u'<img src="%s" width="75" height="75"  >' % get_thumbnail(self.cover, '75x75', crop='center', quality=99).url
        else:
            return '(none)'
    img_thumbs_preview.short_description = u'Миниатюра'
    img_thumbs_preview.allow_tags        = True

    class Meta:
        verbose_name        = u'Положения для студентов'
        verbose_name_plural = u'Положения для студентов'
        ordering            = ['id']
        get_latest_by       = "-id"

    def __unicode__(self):
        return u'%s'%self.name

class StudPositionPlugin(CMSPlugin):
    stud_position = models.ForeignKey(StudPosition)

class BudgetPlugin(CMSPlugin):
    budget = models.ForeignKey(Budget)

class LicensePlugin(CMSPlugin):
    license = models.ForeignKey(License)

class LocalActPlugin(CMSPlugin):
    localact = models.ForeignKey(LocalAct)