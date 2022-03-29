from django.db import models


class SendNumber(models.Model):
    phone = models.CharField(max_length=50)
    create_date = models.DateField(auto_now=True)
    create_time = models.TimeField(auto_now=True)
    ip = models.CharField(blank=True, max_length=50)

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = 'Send Number Form'
        verbose_name_plural = 'Send Number Form'


class Aloqa(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    email = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=50)
    message = models.TextField(max_length=1000)
    create_date = models.DateField(auto_now=True)
    create_time = models.TimeField(auto_now=True)
    ip = models.CharField(blank=True, max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Aloqa Formasi'
        verbose_name_plural = 'Aloqa Formasi'
