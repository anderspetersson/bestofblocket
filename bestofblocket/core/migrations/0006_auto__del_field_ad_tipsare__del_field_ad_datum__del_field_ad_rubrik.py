# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Ad.tipsare'
        db.delete_column(u'core_ad', 'tipsare')

        # Deleting field 'Ad.datum'
        db.delete_column(u'core_ad', 'datum')

        # Deleting field 'Ad.rubrik'
        db.delete_column(u'core_ad', 'rubrik')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Ad.tipsare'
        raise RuntimeError("Cannot reverse this migration. 'Ad.tipsare' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Ad.datum'
        raise RuntimeError("Cannot reverse this migration. 'Ad.datum' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Ad.rubrik'
        raise RuntimeError("Cannot reverse this migration. 'Ad.rubrik' and its values cannot be restored.")

    models = {
        u'core.ad': {
            'Meta': {'object_name': 'Ad'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'filnamn': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tips_author': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['core']