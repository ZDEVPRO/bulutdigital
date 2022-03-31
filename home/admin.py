from django.contrib import admin
from home.models import HomeTitle, HomeLogo, HomeAboutSection, HomeAboutSection2, Portfolio



class HomeTitleAdmin(admin.ModelAdmin):
    list_display = ['title', 'button1', 'button2']


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag']
    readonly_fields = ['image_tag']
    prepopulated_fields = {'slug': ('title',)}


class HomeAboutSection2Admin(admin.ModelAdmin):
    list_display = ['title', 'description']

admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(HomeAboutSection2, HomeAboutSection2Admin)
admin.site.register(HomeAboutSection)
admin.site.register(HomeLogo)
admin.site.register(HomeTitle, HomeTitleAdmin)
