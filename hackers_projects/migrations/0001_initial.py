# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Profile'
        db.create_table('hackers_projects_profile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('remote_id', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('access_token', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('imported_repos', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('hackers_projects', ['Profile'])

        # Adding model 'Repository'
        db.create_table('hackers_projects_repository', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('remote_id', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('shared', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hackers_projects.Profile'])),
        ))
        db.send_create_signal('hackers_projects', ['Repository'])

        # Adding model 'Project'
        db.create_table('hackers_projects_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('submited', self.gf('django.db.models.fields.DateTimeField')()),
            ('votes', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('repository', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hackers_projects.Repository'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hackers_projects.Profile'])),
        ))
        db.send_create_signal('hackers_projects', ['Project'])

        # Adding M2M table for field voted_by on 'Project'
        db.create_table('hackers_projects_project_voted_by', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['hackers_projects.project'], null=False)),
            ('profile', models.ForeignKey(orm['hackers_projects.profile'], null=False))
        ))
        db.create_unique('hackers_projects_project_voted_by', ['project_id', 'profile_id'])

        # Adding model 'Comment'
        db.create_table('hackers_projects_comment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hackers_projects.Project'])),
        ))
        db.send_create_signal('hackers_projects', ['Comment'])


    def backwards(self, orm):
        # Deleting model 'Profile'
        db.delete_table('hackers_projects_profile')

        # Deleting model 'Repository'
        db.delete_table('hackers_projects_repository')

        # Deleting model 'Project'
        db.delete_table('hackers_projects_project')

        # Removing M2M table for field voted_by on 'Project'
        db.delete_table('hackers_projects_project_voted_by')

        # Deleting model 'Comment'
        db.delete_table('hackers_projects_comment')


    models = {
        'hackers_projects.comment': {
            'Meta': {'object_name': 'Comment'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hackers_projects.Project']"})
        },
        'hackers_projects.profile': {
            'Meta': {'object_name': 'Profile'},
            'access_token': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imported_repos': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'remote_id': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
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
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'remote_id': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'shared': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hackers_projects.Profile']"})
        }
    }

    complete_apps = ['hackers_projects']