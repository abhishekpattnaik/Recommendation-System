import json
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from recommend_app import serializers
from recommend_app.scripts.tf_idf_helper import get_all_values, recommended_article_list
from recommend_app.models import url_details, app_user, super_user, recommended_article
from rest_framework.permissions import IsAuthenticated 

class url_view(APIView):
	''' creates the view

	 '''
	def get(self,request):
		url_det = url_details.objects.all()
		url_ser = serializers.UrlSerializer(url_det, many=True)
		return Response(url_ser.data)

	def post(self, request):
		data = request.data.get('input_str')
		if data == 'True':
			urls_dict = get_all_values()
			print('check')
			for url_id in urls_dict:
				url_det = url_details.objects.create(url=urls_dict[url_id]['url'], title=urls_dict[url_id]['title'], uid=url_id)
				print(url_det)
				url_det.save()
			return Response('Success', status=200)
		return Response('Bad request', status=400)


class app_user_view(APIView):
	''' this will create the sub user view '''
	permission_classes = (IsAuthenticated,) 
	def get(self,request):
		url_det = recommended_article.objects.all()
		url_ser = serializers.RecommendedSerializer(url_det, many=True)
		return Response(url_ser.data)

	def post(self, request):
		data = request.data.get('input_doc_id')
		user, new = app_user.objects.get_or_create(username=request.user)
		url = url_details.objects.get(uid=str(data))
		if len(user.liked_urls.filter(uid=str(data))) is 0: 
			user.liked_urls.add(url)
		return Response('liked this page', status=200)


class super_user_view(APIView):
	''' this will create the super user view '''
	permission_classes = (IsAuthenticated,)
	def get(self, request):
		try:
			super_user.objects.get(super_user_name=request.user)
			url_det = app_user.objects.all()
			url_ser = serializers.AppUserSerializer(url_det, many=True)
			return Response(url_ser.data)
		except:
			return Response('User does not exist', status=404)

	def post(self, request):
		data = request.data.get('username')
		sub_user = app_user.objects.get(username=data)
		recommend_url = recommended_article.objects.get(user=data)
		temp_list = list()
		for url in list(sub_user.liked_urls.values()): 
			temp_list.append(url['uid'])
		new_list = recommended_article_list(temp_list)
		for url_id in new_list:
			ud = url_details.objects.get(uid=url_id)
			recommend_url.liked_urls.add(ud)
		return Response(new_list)