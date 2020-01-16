from rest_framework import serializers
from recommend_app.models import url_details, app_user, recommended_article, super_user

class UrlSerializer(serializers.ModelSerializer):
	class Meta:
		model = url_details
		fields = '__all__'

class AppUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = app_user
		fields = '__all__'

class RecommendedSerializer(serializers.ModelSerializer):
	class Meta:
		model = recommended_article
		fields = '__all__'

class SuperUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = super_user
		fields = '__all__'