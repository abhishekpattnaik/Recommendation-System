import json
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated 
from recommend_app import serializers
from recommend_app.scripts.tf_idf_helper import get_all_values, recommended_article_list
from recommend_app.models import UrlDetails, RecommendedArticle, AppUser, SuperUser

class MainUrlView(viewsets.ModelViewSet):
    ''' shows the paginated url details  '''
    queryset = UrlDetails.objects.all()
    serializer_class = serializers.UrlSerializer


class AppUserView(APIView):
    ''' this will create the sub user view '''
    permission_classes = (IsAuthenticated,) 
    def get(self,request):
        url_det = RecommendedArticle.objects.all()
        url_ser = serializers.RecommendedSerializer(url_det, many=True)
        return Response(url_ser.data)

    def post(self, request):
        data = request.data.get('input_doc_id')
        user, new = AppUser.objects.get_or_create(username=request.user)
        url = UrlDetails.objects.get(uid=str(data))
        if len(user.liked_urls.filter(uid=str(data))) is 0: 
            user.liked_urls.add(url)
        return Response('liked this page', status=200)


class SuperUserView(APIView):
    ''' this will create the super user view '''
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        try:
            SuperUser.objects.get(super_user_name=request.user)
            url_det = AppUser.objects.all()
            url_ser = serializers.AppUserSerializer(url_det, many=True)
            return Response(url_ser.data)
        except:
            return Response('User does not exist', status=404)

    def post(self, request):
        data = request.data.get('username')
        sub_user = AppUser.objects.get(username=data)
        recommend_url, new = RecommendedArticle.objects.get_or_create(user=data)
        temp_list = list()
        for url in list(sub_user.liked_urls.values()): 
            temp_list.append(url['uid'])
        new_list = recommended_article_list(temp_list)
        for url_id in new_list:
            ud = UrlDetails.objects.get(uid=url_id)
            recommend_url.liked_urls.add(ud)
        return Response(new_list)
