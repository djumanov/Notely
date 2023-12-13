from django.contrib import admin

from .models import Category, Priority, Note

admin.site.register([Category, Priority, Note])
