from django.contrib import admin
from .models import Category, Tag, Article, Comment, AdditionalText, AdditionalPicture


# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at']
    list_filter = ['category', 'created_at']
    date_hierarchy = 'created_at'
    filter_horizontal = ('tags', )




admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
admin.site.register(AdditionalText)
admin.site.register(AdditionalPicture)
