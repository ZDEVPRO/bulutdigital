from home.models import HomeTitle, HomeLogo, HomeAboutSection, HomeAboutSection2, Portfolio, SendNumberSection, \
    FooterData
from blog.models import RichBlog, HomeBlog, RichHomeBlog


def footer_data_view(request):
    footer_data = FooterData.objects.all().order_by('?')[:3]
    context = {
        'footer_data': footer_data,
    }
    return context


def send_number_section_view(request):
    send_number_section = SendNumberSection.objects.all().order_by('?')[:3]
    context = {
        'send_number_section': send_number_section,
    }
    return context


def rich_home_blog_view(request):
    rich_home_blog = RichHomeBlog.objects.all().order_by('?')[:3]
    context = {
        'rich_home_blog': rich_home_blog,
    }
    return context


def rich_blog_view(request):
    rich_blog_latest = RichBlog.objects.all().order_by('?')[:50]
    context = {
        'rich_blog_latest': rich_blog_latest,
    }
    return context


def portfolio_view(request):
    portfolio_latest = Portfolio.objects.all().order_by('-id')[:3]
    context = {
        'portfolio_latest': portfolio_latest,
    }
    return context


def home_blog_view(request):
    home_blog_latest = HomeBlog.objects.all().order_by('-id')[:3]
    context = {
        'home_blog_latest': home_blog_latest,
    }
    return context


def home_about_section_view(request):
    home_about_section = HomeAboutSection.objects.all().order_by('-id')[:1]
    context = {
        'home_about_section': home_about_section,
    }
    return context


def home_about_section2_view(request):
    home_about_section2 = HomeAboutSection2.objects.all().order_by('-id')[:1]
    context = {
        'home_about_section2': home_about_section2,
    }
    return context


def home_title_view(request):
    home_title = HomeTitle.objects.all().order_by('-id')[:1]
    context = {
        'home_title': home_title,
    }
    return context


def home_logo_view(request):
    home_logo = HomeLogo.objects.all().order_by('-id')[:1]
    context = {
        'home_logo': home_logo,
    }
    return context
