# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        (b'djecks', b'0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name=b'Card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                (b'title', models.CharField(max_length=255, blank=True)),
                (b'description', models.TextField(blank=True)),
                (b'image_front', models.ImageField(null=True, upload_to=b'djecks/cards/images', blank=True)),
                (b'image_back', models.ImageField(null=True, upload_to=b'djecks/images', blank=True)),
                (b'cases', models.ManyToManyField(to=b'djecks.Case', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
