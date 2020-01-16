from rest_framework import serializers
from recommend_app.models import url_details, app_user, recommended_article, super_user

class UrlSerializer(serializers.ModelSerializer):
	''' serialilzes the url details model '''
	class Meta:
		model = url_details
		fields = '__all__'

class AppUserSerializer(serializers.ModelSerializer):
	''' serializes the app user model '''
	class Meta:
		model = app_user
		fields = '__all__'

class RecommendedSerializer(serializers.ModelSerializer):
	''' serializes the recommendation model '''
	class Meta:
		model = recommended_article
		fields = '__all__'

class SuperUserSerializer(serializers.ModelSerializer):
	''' serializes the super user model '''
	class Meta:
		model = super_user
		fields = '__all__'