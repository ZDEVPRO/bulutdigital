# Generated by Django 4.0.3 on 2022-03-28 13:58

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='title',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
