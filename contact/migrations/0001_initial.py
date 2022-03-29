# Generated by Django 4.0.3 on 2022-03-28 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SendNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=50)),
                ('create_date', models.DateField(auto_now=True)),
                ('create_time', models.TimeField(auto_now=True)),
                ('ip', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'verbose_name': 'Send Number Form',
                'verbose_name_plural': 'Send Number Form',
            },
        ),
    ]
