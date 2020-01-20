import json
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated 
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from recommend_app import serializers
from recommend_app.scripts.tf_idf_helper import get_all_values, recommended_article_list
from recommend_app.models import UrlDetails, RecommendedArticle, AppUser, SuperUser
from rest_framework.status import (HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK)
from django.contrib.auth.models import User

class MainUrlView(viewsets.ModelViewSet):
    """
    API endpoint that allows users to view paginated url details 
    """
    queryset = UrlDetails.objects.all()
    serializer_class = serializers.UrlSerializer


class Login(APIView):
    '''
    API endpoint that allows user to login
    '''
    permission_classes = (AllowAny,) 
    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'},status=HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        print(user)
        if not user:
            return Response({'error': 'Invalid Credentials'},status=HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key},status=HTTP_200_OK)


class RegisterUser(APIView):
    ''' 
    API endpoint that allows user to register a new user
    username: 'enter the user name'
    first name: ' enter the first name '
    last name: ' enter the last name '
    password1: ' enter the password ' 
    password2: ' enter the password again ' 
    '''
    permission_classes = (AllowAny,) 
    def post(self, request):
        username = request.data.get('username')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        password1 = request.data.get('password1')
        password2 = request.data.get('password2')
        if password1 == password2:
            # user.password = password1
            user = User.objects.create_user(username,None,password1)
            user.first_name = first_name
            user.last_name = last_name
            try:
                user.save()
                return Response('user created')
            except:
                return Response('User already exists')
        else:
            return Response('please check the password')


class AppUserView(APIView):
    '''
     API endpoint that allows users to create the sub user view 
    '''
    permission_classes = (IsAuthenticated,) 
    def get(self,request):
        try:
            url_det = RecommendedArticle.objects.get(user=request.user)
            return Response({'recommmended urls':list(url_det.liked_urls.values())})
        except:
            return redirect('/home/')

    def post(self, request):
        data = request.data.get('input_doc_id')
        user, new = AppUser.objects.get_or_create(username=request.user)
        url = UrlDetails.objects.get(uid=str(data))
        if len(user.liked_urls.filter(uid=str(data))) is 0: 
            user.liked_urls.add(url)
        temp_list = list()
        temp, new = RecommendedArticle.objects.get_or_create(user=request.user)
        temp.delete()
        recommend_url = RecommendedArticle.objects.create(user=request.user)
        rec_list = recommended_article_list([i['uid'] for i in list(user.liked_urls.values())])
        for rec_url in rec_list:
            ud = UrlDetails.objects.get(uid=rec_url['uid'])
            recommend_url.liked_urls.add(ud)
        return Response({'liked_urls':list(user.liked_urls.values()),'recommended list' : rec_list }, status=200)


class SuperUserView(APIView):
    ''' 
    API endpoint that allows users to create the super user view 
    '''
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        try:
            SuperUser.objects.get(super_user_name=request.user)
            url_det = AppUser.objects.all()
            url_ser = serializers.AppUserSerializer(url_det, many=True)
            return Response(url_ser.data)
        except:
            return Response('User does not exist', status=404)

    # def post(self, request):
    #     data = request.data.get('username')
    #     sub_user = AppUser.objects.get(username=data)
    #     recommend_url, new = RecommendedArticle.objects.get_or_create(user=data)
    #     temp_list = list()
    #     for url in list(sub_user.liked_urls.values()): 
    #         temp_list.append(url['uid'])
    #     new_list = recommended_article_list(temp_list)
    #     for url_id in new_list:
    #         ud = UrlDetails.objects.get(uid=url_id)
    #         recommend_url.liked_urls.add(ud)
    #     return Response(new_list)
