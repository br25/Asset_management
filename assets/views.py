import json
from rest_framework import generics, status, views, permissions
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from companies.models import Company
from .models import Asset, AssetDelegation
from .serializers import AssetDelegationSerializer, AssetSerializer
from .permissions import IsOwner
# from core.mixins import TokenInjectionMixin

class AssetList(generics.ListCreateAPIView):
    # authentication_classes = [TokenAuthentication]
    serializer_class = AssetSerializer
    queryset = Asset.objects.all()

    def get_queryset(self):
        queryset = super(AssetList, self).get_queryset()
        queryset = queryset.filter(owner__owner=self.request.user)
        return queryset

    def create(self, request, *args, **kwargs):
        user = self.request.user
        company = Company.objects.get(owner=user)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=company)
        return Response(serializer.data)


class AssetDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssetSerializer
    queryset = Asset.objects.all()
    permission_classes = [IsOwner]
    

class DelegateAsset(generics.ListCreateAPIView):
    serializer_class = AssetDelegationSerializer
    queryset = AssetDelegation.objects.all()
    

    def get(self, request, pk, *args, **kwargs):
        asset = Asset.objects.get(pk=pk)
        if asset.owner.owner != request.user:
            raise ValidationError("Not permitted")

        queryset = super(DelegateAsset, self).get_queryset()
        queryset = queryset.filter(asset__id=pk)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, pk, *args, **kwargs):
        asset = Asset.objects.get(pk=pk)
        if asset.is_assigned is True:
            raise ValidationError("Item already assigned!", code=400)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(asset=asset)

        asset.is_assigned = True
        asset.save()
        return Response(serializer.data)

