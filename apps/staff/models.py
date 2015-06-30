# -*- coding: utf-8 -*-
from django.db import models
from cms.models import CMSPlugin
from sorl.thumbnail import ImageField, get_thumbnail


class StaffGroup(models.Model):
    staffgroupname = models.CharField(u'Название группы сотрудников', max_length=50) 
    order          = models.IntegerField(u'Порядок групп', null=True)

    class Meta:
        verbose_name        = u'Группа струдников'
        verbose_name_plural = u'Группы сотрудников'
        ordering            = ['id']
        get_latest_by       = "-id"

    def __unicode__(self):
        return self.staffgroupname


class Staff(models.Model):
    photo          = ImageField(u'Фото',  upload_to="images/teachers_photos/")
    staffgroup     = models.ForeignKey(StaffGroup, verbose_name="Группа сотрудников", related_name="get_staff", null=True, blank=True)    
    fio            = models.CharField(u'ФИО', max_length=200)
#    name           = models.CharField(u'Имя', max_length=50)
#    patronymic     = models.CharField(u'Отчество', max_length=50)
    date_birthday  = models.DateTimeField(u'Дата рождения', null=True, blank=True)
    explain        = models.CharField(u'Доп. информация', max_length=200, null=True, blank=True)
    post           = models.CharField(u'Должность', max_length=200, null=True, blank=True)
    category       = models.CharField(u'Категория', max_length=200, null=True, blank=True)
    length_of_work = models.CharField(u'Стаж работы', max_length=200, null=True, blank=True)
    education      = models.CharField(u'Образование', max_length=200, null=True, blank=True)

    def photo_preview(self):
        if self.photo:
            return u'<img src="%s"  >' %  get_thumbnail(self.photo, '100x150', crop='center', quality=99).url
        else:
            return '(none)'
    photo_preview.short_description = u'Фото'
    photo_preview.allow_tags        = True

    def admin_show(self):
        return u"%s - %s" % (self.fio, (self.date_birthday.strftime("%d.%m.%y") if self.date_birthday else None))
    admin_show.short_description = u'ФИО - дата рождения'

    class Meta:
        verbose_name        = u'Сотрудник'
        verbose_name_plural = u'Сотрудники'
        ordering            = ['id']
        get_latest_by       = "-id"

    def __unicode__(self):
        return '%s %s' % (self.fio, (self.date_birthday.strftime("%d.%m.%y") if self.date_birthday else None))


class StaffPlugin(CMSPlugin):
    staff = models.ForeignKey(Staff)