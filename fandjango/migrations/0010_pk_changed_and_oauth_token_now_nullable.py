# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'User.id'
        db.delete_column('fandjango_user', 'id')

        # Changing field 'User.oauth_token'
        db.alter_column('fandjango_user', 'oauth_token_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['fandjango.OAuthToken'], unique=True, null=True))

        # Changing field 'User.facebook_id'
        db.alter_column('fandjango_user', 'facebook_id', self.gf('django.db.models.fields.BigIntegerField')(unique=True, primary_key=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'User.id'
        raise RuntimeError("Cannot reverse this migration. 'User.id' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'User.oauth_token'
        #raise RuntimeError("Cannot reverse this migration. 'User.oauth_token' and its values cannot be restored.")

        # Changing field 'User.facebook_id'
        #db.alter_column('fandjango_user', 'facebook_id', self.gf('django.db.models.fields.BigIntegerField')(unique=True))

    models = {
        'fandjango.oauthtoken': {
            'Meta': {'object_name': 'OAuthToken'},
            'expires_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issued_at': ('django.db.models.fields.DateTimeField', [], {}),
            'token': ('django.db.models.fields.TextField', [], {})
        },
        'fandjango.user': {
            'Meta': {'object_name': 'User'},
            'authorized': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'facebook_id': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'facebook_username': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'last_seen_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'oauth_token': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['fandjango.OAuthToken']", 'unique': 'True', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['fandjango']
