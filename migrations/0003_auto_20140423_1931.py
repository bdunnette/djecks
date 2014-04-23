# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        (b'djecks', b'0002_card'),
    ]

    operations = [
        migrations.AddField(
            model_name=b'case',
            name=b'sex',
            field=models.CharField(blank=True, max_length=1, null=True, choices=[(b'F', b'Female'), (b'M', b'Male')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name=b'case',
            name=b'age',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name=b'case',
            name=b'decks',
            field=models.ManyToManyField(to=b'djecks.Deck', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name=b'card',
            name=b'cases',
            field=models.ManyToManyField(to=b'djecks.Case', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name=b'card',
            name=b'image_back',
            field=models.ImageField(null=True, upload_to=b'djecks/cards/images', blank=True),
        ),
    ]
