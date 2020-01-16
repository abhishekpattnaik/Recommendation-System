from django.contrib.auth.models import User,Group
from rest_framework import serializers
from app import models

class UrlSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Url_Details
		fields = '__all__'

class TestSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.test_model
		fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.url_rating
		fields = '__all__'

class LikedSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.user_liked
		fields = '__all__'