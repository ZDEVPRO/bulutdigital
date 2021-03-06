# Generated by Django 4.0.3 on 2022-03-30 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_portfolio_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='pdf',
            field=models.FileField(default='nkdcx', upload_to='pdf/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
