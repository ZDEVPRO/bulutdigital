from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog_view, name='blog'),
    path('blog/<int:id>/<slug:slug>', views.blog_detail_view, name='blog_detail'),
    path('rblog/<int:id>/<slug:slug>', views.rich_blog_detail_view, name='rich_blog_detail'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio-detail/<int:id>/<slug:slug>', views.portfolio_detail_view, name='portfolio_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
