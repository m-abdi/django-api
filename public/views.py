from django.shortcuts import render
from rest_framework import status
from rest_framework.views import Response, APIView
from . import models
from .serializer import LastArticlesSerializer


# view for getting last x published articles(x comes from client)
class LastArticles(APIView):
    # get method
    def get(self, request):
        if "number" in request.GET:
            # get number from request query parameters dictionary(request.GET)
            n = int(request.GET['number'])
            locale = request.GET["locale"]
            # query for all articles then order them by creation date descending
            last_articles = models.Article.objects.filter(
                language=locale).order_by("-created_at")
            # convert the query set to python native dictionary
            serializer = LastArticlesSerializer(last_articles, many=True)
            # convert the dictionary to json format and send it to the front-end
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif "all" in request.GET:
            # query for all articles
            last_articles = models.Article.objects.all()
            # convert the query set to python native dictionary
            serializer = LastArticlesSerializer(last_articles, many=True)
            # convert the dictionary to json format and send it to the front-end
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif "id" in request.GET:
            # query for an specific article
            last_articles = models.Article.objects.get(id=request.GET["id"])
            # convert the query set to python native dictionary
            serializer = LastArticlesSerializer(last_articles)
            # convert the dictionary to json format and send it to the front-end
            return Response(serializer.data, status=status.HTTP_200_OK)
