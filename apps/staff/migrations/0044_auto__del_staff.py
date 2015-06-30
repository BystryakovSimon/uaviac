# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Staff'
        db.delete_table('staff_staff')


    def backwards(self, orm):
        # Adding model 'Staff'
        db.create_table('staff_staff', (
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('patronymic', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('post', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('education', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('length_of_work', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('date_birthday', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('second_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('staff', ['Staff'])


    models = {
        
    }

    complete_apps = ['staff']