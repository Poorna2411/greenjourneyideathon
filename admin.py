from django.contrib import admin
from .models import ContactMessage
from .models import BlogPost

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'id')  # Add any fields you want to display
    search_fields = ('name', 'email')
admin.site.register(ContactMessage, ContactMessageAdmin)

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'content')
admin.site.register(BlogPost, BlogPostAdmin)


