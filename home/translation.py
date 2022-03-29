from modeltranslation.translator import register, TranslationOptions
from home.models import HomeTitle, HomeAboutSection, SendNumberSection, HomeAboutSection2
from blog.models import Blog


@register(HomeTitle)
class HomeTitleTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'button1', 'button2')


@register(HomeAboutSection)
class HomeAboutSectionTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'button_title')
