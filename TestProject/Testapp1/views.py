from django.shortcuts import render
from Testapp1.models import articleModels
from Testapp1.serializers import articleSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from Testapp1.helper import *
class articleDetail(APIView):
    def get(self,request):
        detailsvar = articleModels.objects.all()
        detailSer = articleSerializer(detailsvar,many=True)
        return Response({'Article':detailSer.data})
    def post(self, request, format=None):
        # serializer = articleSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        upload('https://medium.com/the-andela-way/creating-a-django-api-using-django-rest-framework-apiview-b365dca53c1d')
        return Response('created', status=status.HTTP_201_CREATED)