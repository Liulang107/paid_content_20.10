from django.contrib import admin
from .models import Article, Profile

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'paid_content')

@admin.register(Profile)
class Profile(admin.ModelAdmin):
    list_display = ('user', 'subscription')
