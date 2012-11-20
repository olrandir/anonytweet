# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Tweeter', fields ['username']
        db.create_unique('tweeters', ['username'])


    def backwards(self, orm):
        # Removing unique constraint on 'Tweeter', fields ['username']
        db.delete_unique('tweeters', ['username'])


    models = {
        'anonytweet.tweeter': {
            'Meta': {'object_name': 'Tweeter', 'db_table': "'tweeters'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2'})
        }
    }

    complete_apps = ['anonytweet']