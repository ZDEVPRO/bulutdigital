from django.contrib import admin
from contact.models import SendNumber, Aloqa


class SendNumberAdmin(admin.ModelAdmin):
    list_display = ['phone', 'create_time', 'create_date']
    readonly_fields = ['phone', 'create_time', 'create_date', 'ip']


class AloqaAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'phone', 'create_time', 'create_date']
    readonly_fields = ['name', 'subject', 'phone', 'create_time', 'create_date', 'ip']


admin.site.register(Aloqa, AloqaAdmin)
admin.site.register(SendNumber, SendNumberAdmin)
