# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Ad.generation'
        db.add_column(u'core_ad', 'generation',
                      self.gf('django.db.models.fields.SmallIntegerField')(default=0, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Ad.generation'
        db.delete_column(u'core_ad', 'generation')


    models = {
        u'core.ad': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Ad'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'filnamn': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'generation': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'tips_author': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['core']