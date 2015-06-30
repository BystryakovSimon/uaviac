# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Staff'
        db.create_table('main_staff', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('second_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('patronymic', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('date_birthday', self.gf('django.db.models.fields.DateTimeField')()),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('inf', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('main', ['Staff'])

        # Adding model 'StaffPlugin'
        db.create_table('cmsplugin_staffplugin', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('staff', self.gf('django.db.models.fields.related.ForeignKey')(related_name='plugins', to=orm['main.Staff'])),
        ))
        db.send_create_signal('main', ['StaffPlugin'])

        # Adding model 'News'
        db.create_table('main_news', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('short', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('img', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('full', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('main', ['News'])

        # Adding model 'NewsPlugin'
        db.create_table('cmsplugin_newsplugin', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('staff', self.gf('django.db.models.fields.related.ForeignKey')(related_name='plugins', to=orm['main.News'])),
        ))
        db.send_create_signal('main', ['NewsPlugin'])


    def backwards(self, orm):
        # Deleting model 'Staff'
        db.delete_table('main_staff')

        # Deleting model 'StaffPlugin'
        db.delete_table('cmsplugin_staffplugin')

        # Deleting model 'News'
        db.delete_table('main_news')

        # Deleting model 'NewsPlugin'
        db.delete_table('cmsplugin_newsplugin')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
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
        'main.news': {
            'Meta': {'ordering': "['id']", 'object_name': 'News'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'full': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'short': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'main.newsplugin': {
            'Meta': {'object_name': 'NewsPlugin', 'db_table': "'cmsplugin_newsplugin'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'staff': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'plugins'", 'to': "orm['main.News']"})
        },
        'main.staff': {
            'Meta': {'ordering': "['id']", 'object_name': 'Staff'},
            'date_birthday': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inf': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'patronymic': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'second_name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'main.staffplugin': {
            'Meta': {'object_name': 'StaffPlugin', 'db_table': "'cmsplugin_staffplugin'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'staff': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'plugins'", 'to': "orm['main.Staff']"})
        }
    }

    complete_apps = ['main']