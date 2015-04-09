# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('descripciones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='descripcionpost',
            name='prueba',
            field=ckeditor.fields.RichTextField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='descripcionpost',
            name='descripcion',
            field=models.CharField(max_length=255),
            preserve_default=True,
        ),
    ]
