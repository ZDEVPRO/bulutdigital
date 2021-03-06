# Generated by Django 4.0.3 on 2022-03-30 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_portfolio_service_type_en_portfolio_service_type_ru_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('white_logo', models.ImageField(upload_to='images/white_logo/')),
                ('description', models.TextField(max_length=1000)),
                ('telegram', models.CharField(max_length=300)),
                ('instagram', models.CharField(max_length=300)),
                ('linkedin', models.CharField(max_length=300)),
                ('facebook', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name': 'Footer Logo and About',
                'verbose_name_plural': 'Footer Logo About',
            },
        ),
    ]
