from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp', 'is_updated', 'draft', 'author']
    search_fields = ['title', 'content']
    list_editable = ['is_updated', 'draft']


admin.site.register(Post, PostAdmin)
