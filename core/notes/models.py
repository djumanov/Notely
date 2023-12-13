from django.db import models
from accounts.models import UserData

from markdownfield.models import MarkdownField, RenderedMarkdownField
from markdownfield.validators import VALIDATOR_CLASSY


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Priority(models.Model):
    choices = [
        ('Must do', 'Must do'),
        ('Should do', 'Should do'),
        ('Nice to do', 'Nice to do'),
        ('Delegate', 'Delegate'),
        ('Eliminate', 'Eliminate'),
    ]
    name = models.CharField(max_length=20, unique=True, choices=choices)

    def __str__(self):
        return self.name


class Note(models.Model):
    title      = models.CharField(max_length=64)
    content    = MarkdownField(rendered_field='content_rendered', validator=VALIDATOR_CLASSY)
    completed  = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category   = models.ForeignKey(Category, on_delete=models.CASCADE)
    user       = models.ForeignKey(UserData, on_delete=models.CASCADE)
    priority   = models.ForeignKey(Priority, on_delete=models.CASCADE)

    content_rendered = RenderedMarkdownField()

    def __str__(self):
        return self.title
