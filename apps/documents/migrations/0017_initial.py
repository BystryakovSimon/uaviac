# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'LocalAct'
        db.create_table('documents_localact', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('cover', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('act', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('documents', ['LocalAct'])

        # Adding model 'License'
        db.create_table('documents_license', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('license', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
        ))
        db.send_create_signal('documents', ['License'])

        # Adding model 'Budget'
        db.create_table('documents_budget', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('budget', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
        ))
        db.send_create_signal('documents', ['Budget'])

        # Adding model 'StudPosition'
        db.create_table('documents_studposition', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('stud_position', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
        ))
        db.send_create_signal('documents', ['StudPosition'])

        # Adding model 'StudPositionPlugin'
        db.create_table('cmsplugin_studpositionplugin', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('stud_position', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['documents.StudPosition'])),
        ))
        db.send_create_signal('documents', ['StudPositionPlugin'])

        # Adding model 'BudgetPlugin'
        db.create_table('cmsplugin_budgetplugin', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('budget', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['documents.Budget'])),
        ))
        db.send_create_signal('documents', ['BudgetPlugin'])

        # Adding model 'LicensePlugin'
        db.create_table('cmsplugin_licenseplugin', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('license', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['documents.License'])),
        ))
        db.send_create_signal('documents', ['LicensePlugin'])

        # Adding model 'LocalActPlugin'
        db.create_table('cmsplugin_localactplugin', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('localact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['documents.LocalAct'])),
        ))
        db.send_create_signal('documents', ['LocalActPlugin'])


    def backwards(self, orm):
        # Deleting model 'LocalAct'
        db.delete_table('documents_localact')

        # Deleting model 'License'
        db.delete_table('documents_license')

        # Deleting model 'Budget'
        db.delete_table('documents_budget')

        # Deleting model 'StudPosition'
        db.delete_table('documents_studposition')

        # Deleting model 'StudPositionPlugin'
        db.delete_table('cmsplugin_studpositionplugin')

        # Deleting model 'BudgetPlugin'
        db.delete_table('cmsplugin_budgetplugin')

        # Deleting model 'LicensePlugin'
        db.delete_table('cmsplugin_licenseplugin')

        # Deleting model 'LocalActPlugin'
        db.delete_table('cmsplugin_localactplugin')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 11, 14, 0, 0)'}),
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
        'documents.budget': {
            'Meta': {'ordering': "['id']", 'object_name': 'Budget'},
            'budget': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'documents.budgetplugin': {
            'Meta': {'object_name': 'BudgetPlugin', 'db_table': "'cmsplugin_budgetplugin'", '_ormbases': ['cms.CMSPlugin']},
            'budget': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['documents.Budget']"}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'})
        },
        'documents.license': {
            'Meta': {'ordering': "['id']", 'object_name': 'License'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'license': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'documents.licenseplugin': {
            'Meta': {'object_name': 'LicensePlugin', 'db_table': "'cmsplugin_licenseplugin'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'license': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['documents.License']"})
        },
        'documents.localact': {
            'Meta': {'ordering': "['id']", 'object_name': 'LocalAct'},
            'act': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'cover': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'documents.localactplugin': {
            'Meta': {'object_name': 'LocalActPlugin', 'db_table': "'cmsplugin_localactplugin'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'localact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['documents.LocalAct']"})
        },
        'documents.studposition': {
            'Meta': {'ordering': "['id']", 'object_name': 'StudPosition'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'stud_position': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'})
        },
        'documents.studpositionplugin': {
            'Meta': {'object_name': 'StudPositionPlugin', 'db_table': "'cmsplugin_studpositionplugin'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'stud_position': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['documents.StudPosition']"})
        }
    }

    complete_apps = ['documents']