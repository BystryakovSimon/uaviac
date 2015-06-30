# -*- coding: utf-8 -*-
from django.db import models
from cms.models import CMSPlugin

class Book(models.Model):
    group = models.CharField('Группа', max_length=50)
    name  = models.CharField('Название книги', max_length=50)
    book  = models.FileField('Выберите книгу',blank=True, upload_to='books/')

    class Meta:
        verbose_name        = 'Книга'
        verbose_name_plural = 'Книги для заочников'
        ordering            = ['id']
        get_latest_by       = "-id"

    def __unicode__(self):
        return self.name


#class BookPlugin(CMSPlugin):
#    books = models.ForeignKey('books.Book', related_name='plugins')

#    def __unicode__(self):
#        return self.books.name
