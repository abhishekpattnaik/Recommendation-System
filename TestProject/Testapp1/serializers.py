from rest_framework import serializers,exceptions
from Testapp1.models import articleModels
class articleSerializer(serializers.ModelSerializer):
    class Meta:
        model = articleModels
        fields = '__all__'