# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Staff'
        db.create_table('staff_staff', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('second_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('patronymic', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('date_birthday', self.gf('django.db.models.fields.DateTimeField')()),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('inf', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('staff', ['Staff'])


    def backwards(self, orm):
        # Deleting model 'Staff'
        db.delete_table('staff_staff')


    models = {
        'staff.staff': {
            'Meta': {'ordering': "['id']", 'object_name': 'Staff'},
            'date_birthday': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inf': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'patronymic': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'second_name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['staff']