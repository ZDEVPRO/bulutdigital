# Generated by Django 4.0.3 on 2022-03-29 07:17

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_richblog_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='description_en',
            field=models.TextField(blank=True, max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='description_ru',
            field=models.TextField(blank=True, max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='description_uz',
            field=models.TextField(blank=True, max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='text1_en',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='text1_ru',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='text1_uz',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='text2_en',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='text2_ru',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='text2_uz',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='text3_en',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='text3_ru',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='text3_uz',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='title_en',
            field=models.TextField(blank=True, max_length=601, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='title_ru',
            field=models.TextField(blank=True, max_length=601, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='title_uz',
            field=models.TextField(blank=True, max_length=601, null=True),
        ),
        migrations.AddField(
            model_name='richblog',
            name='content_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='richblog',
            name='content_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='richblog',
            name='content_uz',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='richblog',
            name='description_en',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='richblog',
            name='description_ru',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='richblog',
            name='description_uz',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='richblog',
            name='title_en',
            field=models.TextField(blank=True, max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='richblog',
            name='title_ru',
            field=models.TextField(blank=True, max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='richblog',
            name='title_uz',
            field=models.TextField(blank=True, max_length=600, null=True),
        ),
    ]