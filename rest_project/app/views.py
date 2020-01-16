from rest_framework import viewsets
from app import models,serializers
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from rest_framework.parsers import JSONParser
from app.helper import get_all_values, cos_sim, search_word, get_search
from app.models import test_model, user_liked, Url_Details
from rest_framework.permissions import IsAuthenticated 

class url_detail(APIView):
	# permission_classes = (IsAuthenticated,) 
	def get(self,request):
		# wocodo = get_all_values()
		# for c in wocodo:
		# 	created_obj = Url_Details.objects.create(uid = c, title = wocodo[c]['title'], url = wocodo[c]['url'])
		# 	created_obj.save()
		# 	print('inserted',c)
		# print('done')
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
	# permission_classes = (IsAuthenticated,) 
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



class like_url(APIView):
	# permission_classes = (IsAuthenticated,) 
	def get(self,request):
		url_det = models.user_liked.objects.all()
		url_ser = serializers.LikedSerializer(url_det, many=True)
		# print('user = ',request.user)
		return Response(url_ser.data)
		# return Response(request.user)

	def post(self, request):
		# data = requeszt.data.get('input_doc_id')
		# dd = cos_s = user_likedim(data)
		# user1 = models.user_liked.objects.get_or_create(username=request.user)
		# user = user1[0]
		# user.save()
		# url = models.test_model.objects.get(uid=data)
		# user.liked_urls.add(url)
		return Response('liked this page', status=200)

class super_admin(APIView):
	# permission_classes = (IsAuthenticated,)
	def get(self, request):
		# try:
		# 	super_admin
		url_det = models.user_liked.objects.all()
		url_ser = serializers.LikedSerializer(url_det, many=True)

class create_super_admin(APIView):
	def post(self, request):
		