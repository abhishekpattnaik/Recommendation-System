from django.contrib.auth.models import User,Group
from rest_framework import serializers
from app import models

class FriendSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Friend
		fields = ('id', 'name')

class BelongingSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Belonging 
		fields = ('id', 'name')

class BorrowedSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Borrowed 
		fields = ('id', 'what', 'to_who', 'when', 'returned')

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