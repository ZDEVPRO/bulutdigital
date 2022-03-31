from modeltranslation.translator import register, TranslationOptions
from home.models import HomeTitle, HomeAboutSection, Portfolio, SendNumberSection, HomeAboutSection2
from blog.models import Blog, RichBlog
from footer.models import FooterMenuMeta, FooterServiceMeta, FooterData


@register(FooterData)
class FooterDataTranslationOptions(TranslationOptions):
    fields = ('description',)


@register(FooterMenuMeta)
class FooterMenuMetaTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(FooterServiceMeta)
class FooterServiceMetaTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(HomeTitle)
class HomeTitleTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'button1', 'button2')


@register(HomeAboutSection)
class HomeAboutSectionTranslationOptions(TranslationOptions):
    fields = ('content',)


@register(HomeAboutSection2)
class HomeAboutSection2TranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'button_title')


@register(RichBlog)
class RichBlogTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'content')


@register(Blog)
class RichBlogTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'text1', 'text2', 'text3')


@register(SendNumberSection)
class SendNumberSectionTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'button_title')


@register(Portfolio)
class SendNumberSectionTranslationOptions(TranslationOptions):
    fields = ('title', 'description1', 'description2', 'service_type')
