from django.contrib import admin
from blogApp.models import Blog

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display=('id', 'author', 'title', 'content')

admin.site.register(Blog, BlogAdmin)