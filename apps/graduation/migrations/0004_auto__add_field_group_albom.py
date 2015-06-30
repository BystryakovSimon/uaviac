# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Group.albom'
        db.add_column('graduation_group', 'albom',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gallery.Albom'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Group.albom'
        db.delete_column('graduation_group', 'albom_id')


    models = {
        'gallery.albom': {
            'Meta': {'ordering': "['id']", 'object_name': 'Albom'},
            'cover': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 23, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'graduation.graduation': {
            'Meta': {'ordering': "['id']", 'object_name': 'Graduation'},
            'albom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Albom']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'graduation.group': {
            'Meta': {'ordering': "['id']", 'object_name': 'Group'},
            'albom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Albom']", 'null': 'True', 'blank': 'True'}),
            'form_master': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'graduation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'get_groups'", 'to': "orm['graduation.Graduation']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'specialty': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'graduation.student': {
            'Meta': {'ordering': "['id']", 'object_name': 'Student'},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'get_students'", 'to': "orm['graduation.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'patronymic': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'second_name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['graduation']