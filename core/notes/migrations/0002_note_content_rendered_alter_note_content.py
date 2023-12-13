# Generated by Django 5.0 on 2023-12-13 15:59

import markdownfield.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='content_rendered',
            field=markdownfield.models.RenderedMarkdownField(default='fdsaf'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='note',
            name='content',
            field=markdownfield.models.MarkdownField(rendered_field='content_rendered'),
        ),
    ]
