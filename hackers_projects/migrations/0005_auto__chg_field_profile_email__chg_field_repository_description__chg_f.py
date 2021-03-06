# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Profile.email'
        db.alter_column('hackers_projects_profile', 'email', self.gf('django.db.models.fields.CharField')(max_length=300, null=True))

        # Changing field 'Repository.description'
        db.alter_column('hackers_projects_repository', 'description', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Repository.url'
        db.alter_column('hackers_projects_repository', 'url', self.gf('django.db.models.fields.CharField')(max_length=300, null=True))

        # Changing field 'Repository.name'
        db.alter_column('hackers_projects_repository', 'name', self.gf('django.db.models.fields.CharField')(max_length=300, null=True))

    def backwards(self, orm):

        # Changing field 'Profile.email'
        db.alter_column('hackers_projects_profile', 'email', self.gf('django.db.models.fields.CharField')(default=None, max_length=300))

        # Changing field 'Repository.description'
        db.alter_column('hackers_projects_repository', 'description', self.gf('django.db.models.fields.TextField')(default=None))

        # Changing field 'Repository.url'
        db.alter_column('hackers_projects_repository', 'url', self.gf('django.db.models.fields.CharField')(default=None, max_length=300))

        # Changing field 'Repository.name'
        db.alter_column('hackers_projects_repository', 'name', self.gf('django.db.models.fields.CharField')(default=None, max_length=300))

    models = {
        'hackers_projects.comment': {
            'Meta': {'object_name': 'Comment'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hackers_projects.Project']"}),
            'submited': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hackers_projects.Profile']", 'null': 'True'})
        },
        'hackers_projects.profile': {
            'Meta': {'object_name': 'Profile'},
            'access_token': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imported_repos': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'remote_id': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        'hackers_projects.project': {
            'Meta': {'object_name': 'Project'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'repository': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hackers_projects.Repository']"}),
            'submited': ('django.db.models.fields.DateTimeField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hackers_projects.Profile']"}),
            'voted_by': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'votes'", 'symmetrical': 'False', 'to': "orm['hackers_projects.Profile']"}),
            'votes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        'hackers_projects.repository': {
            'Meta': {'object_name': 'Repository'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'remote_id': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'shared': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hackers_projects.Profile']"})
        }
    }

    complete_apps = ['hackers_projects']