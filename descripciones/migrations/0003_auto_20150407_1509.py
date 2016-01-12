# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('descripciones', '0002_auto_20150407_1509'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='descripcionpost',
            name='prueba',
        ),
        migrations.AlterField(
            model_name='descripcionpost',
            name='descripcion',
            field=ckeditor.fields.RichTextField(),
            preserve_default=True,
        ),
    ]
