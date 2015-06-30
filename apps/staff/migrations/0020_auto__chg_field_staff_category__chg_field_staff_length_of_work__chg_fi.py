# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Staff.category'
        db.alter_column('staff_staff', 'category', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Staff.length_of_work'
        db.alter_column('staff_staff', 'length_of_work', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Staff.photo'
        db.alter_column('staff_staff', 'photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

        # Changing field 'Staff.date_birthday'
        db.alter_column('staff_staff', 'date_birthday', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'Staff.post'
        db.alter_column('staff_staff', 'post', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Staff.education'
        db.alter_column('staff_staff', 'education', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

    def backwards(self, orm):

        # Changing field 'Staff.category'
        db.alter_column('staff_staff', 'category', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Staff.length_of_work'
        db.alter_column('staff_staff', 'length_of_work', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'Staff.photo'
        db.alter_column('staff_staff', 'photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100))

        # Changing field 'Staff.date_birthday'
        db.alter_column('staff_staff', 'date_birthday', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Staff.post'
        db.alter_column('staff_staff', 'post', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Staff.education'
        db.alter_column('staff_staff', 'education', self.gf('django.db.models.fields.CharField')(max_length=200))

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
        'staff.staff': {
            'Meta': {'ordering': "['id']", 'object_name': 'Staff'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'date_birthday': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'education': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length_of_work': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'patronymic': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'post': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'second_name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'staff.staffplugin': {
            'Meta': {'object_name': 'StaffPlugin', 'db_table': "'cmsplugin_staffplugin'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'staff': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'plugins'", 'to': "orm['staff.Staff']"})
        }
    }

    complete_apps = ['staff']