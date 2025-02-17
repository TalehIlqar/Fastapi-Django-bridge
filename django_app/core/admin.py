from django.contrib import admin
from parler.admin import TranslatableAdmin

from .models import  Book, Author


@admin.register(Book)
class BookAdmin(TranslatableAdmin):
    list_display = ("title",)
    search_fields = ("translations__description", "translations__title")


@admin.register(Author)
class AuthorAdmin(TranslatableAdmin):
    list_display = ("name",)
    search_fields = ("translations__bio", "name")