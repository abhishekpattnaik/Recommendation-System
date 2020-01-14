from rest_framework import viewsets
from app import models,serializers
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from rest_framework.parsers import JSONParser
from app.helper import get_all_values, cos_sim, search_word, get_search
from app.models import test_model
from rest_framework.permissions import IsAuthenticated 

class FriendViewset(viewsets.ModelViewSet):
    queryset = models.Friend.objects.all()
    serializer_class = serializers.FriendSerializer


class BelongingViewset(viewsets.ModelViewSet):
    queryset = models.Belonging.objects.all()
    serializer_class = serializers.BelongingSerializer


class BorrowedViewset(viewsets.ModelViewSet):
    queryset = models.Borrowed.objects.all()
    serializer_class = serializers.BorrowedSerializer

class url_detail(APIView):
	permission_classes = (IsAuthenticated,) 
	def get(self,request):
		url_det = models.Url_Details.objects.all()
		url_ser = serializers.UrlSerializer(url_det, many=True)
		return Response(url_ser.data)

	def post(self, request):
		data = request.data
		serializer = serializers.UrlSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			print(serializer.data.get('url'))
			return Response("Success", status=201)
		return Response(serializer.errors, status=400)




class test_detail(APIView):
	permission_classes = (IsAuthenticated,) 
	def get(self,request):
		url_det = models.test_model.objects.all()
		url_ser = serializers.TestSerializer(url_det, many=True)
		return Response(url_ser.data)

	def post(self, request):
		data = request.data.get('input_str')
		dd = get_search(data)
		json_dump = json.dumps(dd)
		jsf = json.loads(json_dump)
		return Response(jsf, status=200)




class rating_detail(APIView):
	def get(self,request):
		url_det = models.Url_Details.objects.all()
		url_ser = serializers.UrlSerializer(url_det, many=True)
		return Response(url_ser.data)

	def post(self, request):
		data = request.data
		serializer = serializers.UrlSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			print(serializer.data.get('url'))
			return Response("Success", status=201)
		return Response(serializer.errors, status=400)

