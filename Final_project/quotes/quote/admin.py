from django.contrib import admin
from .models import Author, Tag, Quote
# Register your models here.




class AuthorAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']
    search_fields = ['name']


class TagAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']
    search_fields = ['name']


class QuoteAdmin(admin.ModelAdmin):
    list_display = ['pk', 'text', 'author']
    search_fields = ['author']
    list_filter = ['author']

admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Quote, QuoteAdmin)