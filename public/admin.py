from django.contrib import admin
from .models import Article
from django.db import models
from tinymce.widgets import TinyMCE


class ArticleAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {"widget": TinyMCE(attrs={"cols": 80, "rows": 30})},
    }


admin.site.register(Article, ArticleAdmin)
