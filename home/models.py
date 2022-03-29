from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.safestring import mark_safe


class HomeTitle(models.Model):
    title = models.TextField('Bosh sarlavha', max_length=200)
    description = models.TextField('Malumot', max_length=500)
    button1 = models.CharField('Knopka 1', max_length=100)
    slug_button1 = models.CharField('Knopka 1 Link', max_length=100)
    button2 = models.CharField('Knopka 2', max_length=100)
    slug_button2 = models.CharField('Knopka 2 Link', max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Home Title'
        verbose_name_plural = 'Home Title'


class HomeLogo(models.Model):
    white_logo = models.ImageField(upload_to='images/logo/')
    dark_logo = models.ImageField(upload_to='images/logo/')

    class Meta:
        verbose_name = 'Home Logo'
        verbose_name_plural = 'Home Logo'


class HomeAboutSection(models.Model):
    title = models.TextField(max_length=400)
    description = models.TextField(max_length=1000)

    button_title = models.CharField(max_length=300)
    button_link = models.CharField(max_length=300)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Home About Section'
        verbose_name_plural = 'Home About Section'


class HomeAboutSection2(models.Model):
    title = models.TextField(max_length=401)
    description = models.TextField(max_length=1000)

    button_title = models.CharField(max_length=300)
    button_link = models.CharField(max_length=300)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Home About Section 2'
        verbose_name_plural = 'Home About Section 2'


class SendNumberSection(models.Model):
    title = models.TextField(max_length=500)
    description = models.TextField(max_length=500)

    button_title = models.TextField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Send Number Section'
        verbose_name_plural = 'Send Number Section'


class Portfolio(models.Model):
    title = RichTextField()
    image = models.ImageField(max_length=500)
    link = models.CharField(max_length=500)

    def __str__(self):
        return self.link

    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolio'

    def image_tag(self):
        return mark_safe('<img src="{}" height="50">'.format(self.image.url))

    image_tag.short_description = 'Image'
