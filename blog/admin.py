from django.contrib import admin
from .models import Blog, Tag, Photo

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'photo', 'tag', 'created_datetime', 'updated_datetime')
    list_display_links = ('id', 'title')

class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'text')
    list_display_links = ('id', 'name')

class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')
    list_display_links = ('id', 'name', 'image')

admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Photo, ImageAdmin)
