from django.db import models

from ckeditor.fields import RichTextField
from parler.models import TranslatableModel, TranslatedFields

from core.models import BaseModel

class Category(BaseModel, TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=255),
    )

class News(BaseModel, TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=255),
        description=RichTextField(),
    )
    category = models.ForeignKey(
        'news.Category',
        on_delete=models.CASCADE,
        related_name='news'
    )