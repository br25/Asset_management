from rest_framework import serializers
from .models import Asset, AssetDeligation
from companies.models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError



class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'

class AssetDeligationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetDeligation
        fields = '__all__'

