# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Ad.filnamn'
        db.delete_column(u'core_ad', 'filnamn')

        # Deleting field 'Ad.tips_author'
        db.delete_column(u'core_ad', 'tips_author')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Ad.filnamn'
        raise RuntimeError("Cannot reverse this migration. 'Ad.filnamn' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Ad.tips_author'
        raise RuntimeError("Cannot reverse this migration. 'Ad.tips_author' and its values cannot be restored.")

    models = {
        u'core.ad': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Ad'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'generation': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'core.link': {
            'Meta': {'object_name': 'Link'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['core']