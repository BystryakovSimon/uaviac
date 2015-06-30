# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'News'
        db.create_table('news_news', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 10, 22, 0, 0))),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('short', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('cover', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('full', self.gf('ckeditor.fields.RichTextField')()),
            ('albom', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='get_Albom_by_n', null=True, to=orm['media.Albom'])),
        ))
        db.send_create_signal('news', ['News'])

        # Adding model 'NewsPlugin'
        db.create_table('cmsplugin_newsplugin', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('news', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['news.News'])),
        ))
        db.send_create_signal('news', ['NewsPlugin'])


    def backwards(self, orm):
        # Deleting model 'News'
        db.delete_table('news_news')

        # Deleting model 'NewsPlugin'
        db.delete_table('cmsplugin_newsplugin')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 10, 22, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'media.albom': {
            'Meta': {'ordering': "['-id']", 'object_name': 'Albom'},
            'cover': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 10, 22, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'news.news': {
            'Meta': {'ordering': "['-id']", 'object_name': 'News'},
            'albom': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'get_Albom_by_n'", 'null': 'True', 'to': "orm['media.Albom']"}),
            'cover': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 10, 22, 0, 0)'}),
            'full': ('ckeditor.fields.RichTextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'short': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'news.newsplugin': {
            'Meta': {'object_name': 'NewsPlugin', 'db_table': "'cmsplugin_newsplugin'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'news': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['news.News']"})
        }
    }

    complete_apps = ['news']