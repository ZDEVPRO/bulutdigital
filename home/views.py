from django.core.paginator import Paginator
from blog.models import Blog, RichBlog
from home.forms import SendNumberForm
from contact.models import SendNumber

from django.shortcuts import render, redirect
from home.forms import AloqaForm
from contact.models import Aloqa
from django.contrib import messages


# Create your views here.
def index(request):
    if request.method == 'POST':
        send_form = SendNumberForm(request.POST)
        if send_form.is_valid():
            data = SendNumber()
            data.phone = send_form.cleaned_data['phone']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, 'Yangi xabar keldi!')
            return redirect('index')
    send_form = SendNumberForm
    context = {'send_form': send_form}
    return render(request, 'index/base.html', context)


def contact(request):
    if request.method == 'POST':
        form = AloqaForm(request.POST)
        if form.is_valid():
            data = Aloqa()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.phone = form.cleaned_data['phone']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, 'Yangi xabar keldi!')
            return redirect('contact')
    form = AloqaForm
    context = {'form': form, }
    return render(request, 'contact/base.html', context)


def about(request):
    if request.method == 'POST':
        send_form = SendNumberForm(request.POST)
        if send_form.is_valid():
            data = SendNumber()
            data.phone = send_form.cleaned_data['phone']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, 'Yangi xabar keldi')
            return redirect('index')
    send_form = SendNumberForm
    context = {'send_form': send_form}
    return render(request, 'about/base.html', context)


def blog_view(request):
    blog_latest = Blog.objects.all().order_by('?')[:100]
    paginator = Paginator(blog_latest, per_page=5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'blog_latest': page_obj.object_list,
        'paginator': paginator,
        'page_number': page_number
    }
    return render(request, 'blog/base.html', context)


def blog_detail_view(request, id, slug):
    b_detail = Blog.objects.get(pk=id)
    context = {
        'b_detail': b_detail,
    }
    return render(request, 'blog_detail/base.html', context)


def rich_blog_detail_view(request, id, slug):
    rich_b_detail = RichBlog.objects.get(pk=id)
    context = {
        'rich_b_detail': rich_b_detail,
    }
    return render(request, 'rich_blog_detail/base.html', context)


def portfolio(request):
    return render(request, 'portfolio/base.html')
