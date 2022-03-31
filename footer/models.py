from django.db import models


# Create your models here.
class FooterData(models.Model):
    white_logo = models.ImageField(upload_to='images/white_logo/')
    description = models.TextField(max_length=1000)

    telegram = models.CharField(max_length=300, blank=True)
    instagram = models.CharField(max_length=300, blank=True)
    linkedin = models.CharField(max_length=300, blank=True)
    facebook = models.CharField(max_length=300, blank=True)

    class Meta:
        verbose_name = 'Footer Logo and About'
        verbose_name_plural = 'Footer Logo And About'


class FooterServiceMeta(models.Model):
    title = models.CharField(max_length=500)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Footer Service Meta'
        verbose_name_plural = 'Footer Service Meta'


class FooterMenuMeta(models.Model):
    MENU = (
        ('index', 'Home'),
        ('portfolio', 'Portfolio'),
        ('blog', 'Blog'),
        ('about', 'About'),
        ('contact', 'Contact'),
    )
    title = models.CharField(max_length=300)
    link = models.CharField(choices=MENU, max_length=300)

    class Meta:
        verbose_name = 'Footer Menu Meta'
        verbose_name_plural = 'Footer Menu Meta'
