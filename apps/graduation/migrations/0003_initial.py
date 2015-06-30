# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Graduation'
        db.create_table('graduation_graduation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('albom', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gallery.Albom'], null=True, blank=True)),
        ))
        db.send_create_signal('graduation', ['Graduation'])

        # Adding model 'Group'
        db.create_table('graduation_group', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('graduation', self.gf('django.db.models.fields.related.ForeignKey')(related_name='get_groups', to=orm['graduation.Graduation'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('specialty', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('form_master', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('graduation', ['Group'])

        # Adding model 'Student'
        db.create_table('graduation_student', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('second_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('patronymic', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(related_name='get_students', to=orm['graduation.Group'])),
        ))
        db.send_create_signal('graduation', ['Student'])


    def backwards(self, orm):
        # Deleting model 'Graduation'
        db.delete_table('graduation_graduation')

        # Deleting model 'Group'
        db.delete_table('graduation_group')

        # Deleting model 'Student'
        db.delete_table('graduation_student')


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