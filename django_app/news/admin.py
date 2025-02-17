from django.contrib import admin

from parler.admin import TranslatableAdmin
from .models import News


@admin.register(News)
class BookAdmin(TranslatableAdmin):
    list_display = ("title",)
    search_fields = ("translations__description", "translations__title")
