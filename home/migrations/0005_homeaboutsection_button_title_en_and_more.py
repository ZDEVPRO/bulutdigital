# Generated by Django 4.0.3 on 2022-03-29 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_homeaboutsection_description_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeaboutsection',
            name='button_title_en',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='homeaboutsection',
            name='button_title_ru',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='homeaboutsection',
            name='button_title_uz',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
