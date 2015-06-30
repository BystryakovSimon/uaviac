# -*- coding: utf-8 -*-
from django.db import models
from cms.models import CMSPlugin
from datetime import datetime
from media.models import Albom, AlbomManager
from sorl.thumbnail import ImageField, get_thumbnail
from ckeditor.fields import RichTextField



def get_cover_path(self, file):
    return u"images/news/%s/%s" % (self.title, file)

class NewsManager(models.Manager):
    def get_query_set(self):
        return super(NewsManager, self).get_query_set().filter(is_published=True)

class News(models.Model):
    is_published = models.BooleanField(u'Опубликована', default=True)
    date  = models.DateTimeField(u'Дата новости', default=datetime.now())
    title = models.CharField(u'Заголовок', max_length=100)
    short = models.CharField(u'Выдержка из новости(с тегами)', max_length=100)
    cover = ImageField(u'Обложка новости',  upload_to=u"images/news_covers")
    albom = models.ForeignKey(Albom, verbose_name="Альбом", related_name="get_Albom_by_n", null=True, blank=True)
    full  = RichTextField(u'Полная новость')


    objects      = models.Manager()
    published    = NewsManager()
    
    def cover_preview(self):
        if self.cover:
            return u'<img src="%s"  width="75" height="75" >' %  get_thumbnail(self.cover, '75x75', crop='center', quality=99).url
        else:
            return u'(none)'
    cover_preview.short_description = u'Обложка'
    cover_preview.allow_tags        = True

    class Meta:
        verbose_name        = u'Новость'
        verbose_name_plural = u'Новости'
        ordering            = ['-id']
        get_latest_by       = "-id"

    def __unicode__(self):
        return u'%s %10s' % (self.date.strftime("%d.%m.%y"), self.title)

class NewsPlugin(CMSPlugin):
    news = models.ForeignKey(News)
  