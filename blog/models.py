from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from ckeditor.fields import RichTextField
from django.utils.safestring import mark_safe


class RichBlog(models.Model):
    image = models.ImageField(upload_to='images/blog/', blank=True)
    title = models.TextField(max_length=600, blank=True)
    description = models.TextField(max_length=1000, blank=True)
    slug = models.SlugField(unique=True)
    content = RichTextUploadingField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog Editor'
        verbose_name_plural = 'Blog Editor'

    def image_tag(self):
        return mark_safe('<img src="{}" height="50">'.format(self.image.url))

    image_tag.short_description = 'Image'


class Blog(models.Model):
    title = models.TextField(max_length=601, blank=True)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='images/blog/')
    description = models.TextField(max_length=600, blank=True)
    text1 = models.TextField(max_length=1000, blank=True)
    text2 = models.TextField(max_length=1000, blank=True)
    text3 = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blog'

    def image_tag(self):
        return mark_safe('<img src="{}" height="50">'.format(self.image.url))

    image_tag.short_description = 'Image'


class HomeBlog(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="Blogs")

    class Meta:
        verbose_name = 'Home Blog'
        verbose_name_plural = 'Home Blog'


class RichHomeBlog(models.Model):
    rich_home_blog = models.ForeignKey(RichBlog, on_delete=models.CASCADE, related_name="Richhomeblogs")

    class Meta:
        verbose_name = 'Rich Home Blog'
        verbose_name_plural = 'Rich Home Blog'
