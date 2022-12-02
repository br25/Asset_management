from rest_framework import serializers
from .models import Asset, AssetDelegation
from companies.models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError



class AssetSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(source="owner.name", read_only=True)
    class Meta:
        model = Asset
        fields = '__all__'
        read_only_fields = [
            "owner",
        ]

class AssetDelegationSerializer(serializers.ModelSerializer):
    asset = serializers.CharField(source="asset.name", read_only=True)
    class Meta:
        model = AssetDelegation
        fields = '__all__'
        read_only_fields = [
            "asset",
        ]

