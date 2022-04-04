from django.db import models
from uuid import uuid4
locale_choices = [
    ("en", "English"),
    ("fr", "French"),
]


class Article(models.Model):
    id = models.CharField(default=uuid4, primary_key=True, max_length=500)
    language = models.CharField(
        max_length=100, choices=locale_choices, null=False, blank=False
    )
    title = models.CharField(max_length=200)
    text = models.TextField()
    picture = models.FileField()
    video = models.FileField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
