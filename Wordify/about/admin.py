from django.contrib import admin
from .models import About


# Register your models here.

class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']


admin.site.register(About, AboutAdmin)
