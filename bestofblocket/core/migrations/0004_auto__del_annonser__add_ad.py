# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        db.rename_table('core_annonser', 'core_ad')


    def backwards(self, orm):
        db.rename_table('code_ad','core_annonser') 


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