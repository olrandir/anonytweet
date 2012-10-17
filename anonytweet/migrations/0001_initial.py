# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tweeter'
        db.create_table('tweeters', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('ip', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
        ))
        db.send_create_signal('anonytweet', ['Tweeter'])


    def backwards(self, orm):
        # Deleting model 'Tweeter'
        db.delete_table('tweeters')


    models = {
        'anonytweet.tweeter': {
            'Meta': {'object_name': 'Tweeter', 'db_table': "'tweeters'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        }
    }

    complete_apps = ['anonytweet']