# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Deck'
        db.create_table(u'djecks_deck', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'djecks', ['Deck'])

        # Adding model 'Case'
        db.create_table(u'djecks_case', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('sex', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('age', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'djecks', ['Case'])

        # Adding M2M table for field decks on 'Case'
        m2m_table_name = db.shorten_name(u'djecks_case_decks')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('case', models.ForeignKey(orm[u'djecks.case'], null=False)),
            ('deck', models.ForeignKey(orm[u'djecks.deck'], null=False))
        ))
        db.create_unique(m2m_table_name, ['case_id', 'deck_id'])

        # Adding model 'Card'
        db.create_table(u'djecks_card', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('image_front', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('image_back', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'djecks', ['Card'])

        # Adding M2M table for field cases on 'Card'
        m2m_table_name = db.shorten_name(u'djecks_card_cases')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('card', models.ForeignKey(orm[u'djecks.card'], null=False)),
            ('case', models.ForeignKey(orm[u'djecks.case'], null=False))
        ))
        db.create_unique(m2m_table_name, ['card_id', 'case_id'])


    def backwards(self, orm):
        # Deleting model 'Deck'
        db.delete_table(u'djecks_deck')

        # Deleting model 'Case'
        db.delete_table(u'djecks_case')

        # Removing M2M table for field decks on 'Case'
        db.delete_table(db.shorten_name(u'djecks_case_decks'))

        # Deleting model 'Card'
        db.delete_table(u'djecks_card')

        # Removing M2M table for field cases on 'Card'
        db.delete_table(db.shorten_name(u'djecks_card_cases'))


    models = {
        u'djecks.card': {
            'Meta': {'object_name': 'Card'},
            'cases': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['djecks.Case']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_back': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'image_front': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'djecks.case': {
            'Meta': {'object_name': 'Case'},
            'age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'decks': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['djecks.Deck']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'djecks.deck': {
            'Meta': {'object_name': 'Deck'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['djecks']