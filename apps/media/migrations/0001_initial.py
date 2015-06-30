# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Albom'
        db.create_table('media_albom', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 10, 22, 0, 0))),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('cover', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
        ))
        db.send_create_signal('media', ['Albom'])

        # Adding model 'AlbomPlugin'
        db.create_table('cmsplugin_albomplugin', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('albom', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['media.Albom'])),
        ))
        db.send_create_signal('media', ['AlbomPlugin'])

        # Adding model 'Image'
        db.create_table('media_image', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('alt', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('img', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 10, 22, 0, 0))),
            ('albom', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='get_images', null=True, to=orm['media.Albom'])),
        ))
        db.send_create_signal('media', ['Image'])


    def backwards(self, orm):
        # Deleting model 'Albom'
        db.delete_table('media_albom')

        # Deleting model 'AlbomPlugin'
        db.delete_table('cmsplugin_albomplugin')

        # Deleting model 'Image'
        db.delete_table('media_image')


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
        'media.albomplugin': {
            'Meta': {'object_name': 'AlbomPlugin', 'db_table': "'cmsplugin_albomplugin'", '_ormbases': ['cms.CMSPlugin']},
            'albom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['media.Albom']"}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'})
        },
        'media.image': {
            'Meta': {'ordering': "['id']", 'object_name': 'Image'},
            'albom': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'get_images'", 'null': 'True', 'to': "orm['media.Albom']"}),
            'alt': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 10, 22, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['media']