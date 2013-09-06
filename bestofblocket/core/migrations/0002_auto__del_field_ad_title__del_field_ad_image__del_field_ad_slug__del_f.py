# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Ad.title'
        db.delete_column(u'core_ad', 'title')

        # Deleting field 'Ad.image'
        db.delete_column(u'core_ad', 'image')

        # Deleting field 'Ad.slug'
        db.delete_column(u'core_ad', 'slug')

        # Deleting field 'Ad.date'
        db.delete_column(u'core_ad', 'date')

        # Adding field 'Ad.filnamn'
        db.add_column(u'core_ad', 'filnamn',
                      self.gf('django.db.models.fields.CharField')(default='foo.job', max_length=50),
                      keep_default=False)

        # Adding field 'Ad.rubrik'
        db.add_column(u'core_ad', 'rubrik',
                      self.gf('django.db.models.fields.CharField')(default='foo', max_length=255),
                      keep_default=False)

        # Adding field 'Ad.datum'
        db.add_column(u'core_ad', 'datum',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 7, 23, 0, 0)),
                      keep_default=False)

        # Adding field 'Ad.tipsare'
        db.add_column(u'core_ad', 'tipsare',
                      self.gf('django.db.models.fields.CharField')(default='fooare', max_length=50),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Ad.title'
        raise RuntimeError("Cannot reverse this migration. 'Ad.title' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Ad.image'
        raise RuntimeError("Cannot reverse this migration. 'Ad.image' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Ad.slug'
        raise RuntimeError("Cannot reverse this migration. 'Ad.slug' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Ad.date'
        raise RuntimeError("Cannot reverse this migration. 'Ad.date' and its values cannot be restored.")
        # Deleting field 'Ad.filnamn'
        db.delete_column(u'core_ad', 'filnamn')

        # Deleting field 'Ad.rubrik'
        db.delete_column(u'core_ad', 'rubrik')

        # Deleting field 'Ad.datum'
        db.delete_column(u'core_ad', 'datum')

        # Deleting field 'Ad.tipsare'
        db.delete_column(u'core_ad', 'tipsare')


    models = {
        u'core.ad': {
            'Meta': {'object_name': 'Ad'},
            'datum': ('django.db.models.fields.DateField', [], {}),
            'filnamn': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rubrik': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tipsare': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['core']