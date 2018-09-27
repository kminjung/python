from django.contrib import admin
from noticeApp.models import Notice

# Register your models here.

class NoticeAdmin(admin.ModelAdmin):
    list_display=('id', 'content')

admin.site.register(Notice, NoticeAdmin)