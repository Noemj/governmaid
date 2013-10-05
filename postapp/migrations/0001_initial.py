# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Post'
        db.create_table(u'postapp_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('score', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'postapp', ['Post'])


    def backwards(self, orm):
        # Deleting model 'Post'
        db.delete_table(u'postapp_post')


    models = {
        u'postapp.post': {
            'Meta': {'object_name': 'Post'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['postapp']