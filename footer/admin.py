from django.contrib import admin
from footer.models import FooterData, FooterMenuMeta, FooterServiceMeta


class FooterMenuMetaAdmin(admin.ModelAdmin):
    list_display = ['title', 'link']


admin.site.register(FooterMenuMeta, FooterMenuMetaAdmin)
admin.site.register(FooterData)
admin.site.register(FooterServiceMeta)
