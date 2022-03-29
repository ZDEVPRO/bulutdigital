from django.contrib import admin
from blog.models import Blog, HomeBlog, RichBlog, RichHomeBlog


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image_tag']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['image_tag']


class RichBlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['image_tag']


admin.site.register(RichBlog, RichBlogAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(HomeBlog)
admin.site.register(RichHomeBlog)
