from django.shortcuts import render
from rest_framework.views import APIView
from . import models
from . import serializers
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class Foods(APIView):
    def get(self, request):
        all_foods = models.Food.objects.all()
        serializer = serializers.FoodsSerializer(all_foods, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@method_decorator(csrf_exempt, name='dispatch')
class Orders(APIView):
    def post(self, request):
        serializer = serializers.NewOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
