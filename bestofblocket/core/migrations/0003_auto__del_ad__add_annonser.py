# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Ad'
        db.delete_table(u'core_ad')

        # Adding model 'Annonser'
        db.create_table(u'core_annonser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('filnamn', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('rubrik', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('datum', self.gf('django.db.models.fields.DateField')()),
            ('tipsare', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'core', ['Annonser'])


    def backwards(self, orm):
        # Adding model 'Ad'
        db.create_table(u'core_ad', (
            ('tipsare', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('datum', self.gf('django.db.models.fields.DateField')()),
            ('rubrik', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('filnamn', self.gf('django.db.models.fields.CharField')(max_length=50)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'core', ['Ad'])

        # Deleting model 'Annonser'
        db.delete_table(u'core_annonser')


    models = {
        u'core.annonser': {
            'Meta': {'object_name': 'Annonser'},
            'datum': ('django.db.models.fields.DateField', [], {}),
            'filnamn': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rubrik': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tipsare': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['core']