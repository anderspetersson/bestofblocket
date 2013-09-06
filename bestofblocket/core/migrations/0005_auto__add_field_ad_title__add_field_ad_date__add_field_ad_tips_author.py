# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Ad.title'
        db.add_column(u'core_ad', 'title',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Adding field 'Ad.date'
        db.add_column(u'core_ad', 'date',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 7, 23, 0, 0)),
                      keep_default=False)

        # Adding field 'Ad.tips_author'
        db.add_column(u'core_ad', 'tips_author',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Ad.title'
        db.delete_column(u'core_ad', 'title')

        # Deleting field 'Ad.date'
        db.delete_column(u'core_ad', 'date')

        # Deleting field 'Ad.tips_author'
        db.delete_column(u'core_ad', 'tips_author')


    models = {
        u'core.ad': {
            'Meta': {'object_name': 'Ad'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'datum': ('django.db.models.fields.DateField', [], {}),
            'filnamn': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rubrik': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tips_author': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tipsare': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['core']