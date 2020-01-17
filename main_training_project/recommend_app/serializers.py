from rest_framework import serializers
from recommend_app.models import UrlDetails, RecommendedArticle, AppUser, SuperUser

class UrlSerializer(serializers.ModelSerializer):
	''' serialilzes the url details model '''
	class Meta:
		model = UrlDetails
		fields = '__all__'

class AppUserSerializer(serializers.ModelSerializer):
	''' serializes the app user model '''
	class Meta:
		model = AppUser
		fields = '__all__'

class RecommendedSerializer(serializers.ModelSerializer):
	''' serializes the recommendation model '''
	class Meta:
		model = RecommendedArticle
		fields = '__all__'

class SuperUserSerializer(serializers.ModelSerializer):
	''' serializes the super user model '''
	class Meta:
		model = SuperUser
		fields = '__all__'