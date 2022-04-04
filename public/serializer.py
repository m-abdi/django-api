from rest_framework import serializers
from . import models

class LastArticlesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = models.Article
        fields = "__all__"
