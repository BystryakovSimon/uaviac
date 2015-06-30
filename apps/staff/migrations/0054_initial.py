# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'StaffGroup'
        db.create_table('staff_staffgroup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('staffgroupname', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('staff', ['StaffGroup'])

        # Adding model 'Staff'
        db.create_table('staff_staff', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('staffgroup', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='get_staff', null=True, to=orm['staff.StaffGroup'])),
            ('fio', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('date_birthday', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('explain', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('post', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('length_of_work', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('education', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('staff', ['Staff'])

        # Adding model 'StaffPlugin'
        db.create_table('cmsplugin_staffplugin', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('staff', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['staff.Staff'])),
        ))
        db.send_create_signal('staff', ['StaffPlugin'])


    def backwards(self, orm):
        # Deleting model 'StaffGroup'
        db.delete_table('staff_staffgroup')

        # Deleting model 'Staff'
        db.delete_table('staff_staff')

        # Deleting model 'StaffPlugin'
        db.delete_table('cmsplugin_staffplugin')


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
        'staff.staff': {
            'Meta': {'ordering': "['id']", 'object_name': 'Staff'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'date_birthday': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'education': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'explain': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'fio': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length_of_work': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'post': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'staffgroup': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'get_staff'", 'null': 'True', 'to': "orm['staff.StaffGroup']"})
        },
        'staff.staffgroup': {
            'Meta': {'ordering': "['id']", 'object_name': 'StaffGroup'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'staffgroupname': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'staff.staffplugin': {
            'Meta': {'object_name': 'StaffPlugin', 'db_table': "'cmsplugin_staffplugin'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'staff': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['staff.Staff']"})
        }
    }

    complete_apps = ['staff']