# Generated by Django 4.0.3 on 2022-03-30 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='content',
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='title',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='title_en',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='title_ru',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='title_uz',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
