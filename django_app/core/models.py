from django.db import models
from ckeditor.fields import RichTextField
from parler.models import TranslatableModel, TranslatedFields


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Book(BaseModel, TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=255),
        description=RichTextField(),
    )
    author = models.ForeignKey(
        'core.Author',
        on_delete=models.CASCADE,
        related_name='books'
    )
    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'


class Author(TranslatableModel):
    translations = TranslatedFields(
        bio=models.TextField(null=True, blank=True),
    )
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


class Menu(BaseModel, TranslatableModel):
    slug = models.SlugField(max_length=255, unique=True)
    translations = TranslatedFields(
        title=models.CharField(max_length=255),
        description=RichTextField(),
    )
    image = models.FileField(upload_to='books/', null=True, blank=True)


class Campaign(BaseModel, TranslatableModel):
    slug = models.SlugField(max_length=255, unique=True)
    translations = TranslatedFields(
        title=models.CharField(max_length=255),
        description=RichTextField(),
    )
    image = models.FileField(upload_to='campaigns/', null=True, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


class CampaignForm(BaseModel, TranslatableModel):
    campaign = models.ForeignKey(
        'core.CarModel',
        on_delete=models.CASCADE,
        related_name='forms'
    )
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    message = models.TextField(null=True, blank=True)


class Offer(BaseModel, TranslatableModel):
    slug = models.SlugField(max_length=255, unique=True)
    translations = TranslatedFields(
        title=models.CharField(max_length=255),
        description=RichTextField(),
    )
    image = models.FileField(upload_to='offers/', null=True, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


class Creditİnfo(BaseModel, TranslatableModel):
    slug = models.SlugField(max_length=255, unique=True)
    translations = TranslatedFields(
        title=models.CharField(max_length=255),
        subtitle=models.CharField(max_length=255),
    )
    icon = models.FileField(upload_to='credits/', null=True, blank=True)


class CreditFAQ(BaseModel, TranslatableModel):
    credit_info = models.ForeignKey(
        'core.Creditİnfo',
        on_delete=models.CASCADE,
        related_name='faqs'
    )
    question = models.CharField(max_length=255)
    answer = models.TextField()