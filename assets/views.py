from rest_framework import generics, status, views, permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from .models import Asset
from .serializers import AssetSerializer
from .permissions import IsOwner
# from core.mixins import TokenInjectionMixin

class AssetList(generics.ListCreateAPIView):
    # permission_classes = [IsOwner]
    # authentication_classes = [TokenAuthentication]
    serializer_class = AssetSerializer
    queryset = Asset.objects.all()

    # def get(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     serializer = self.get_serializer(queryset)
    #     return(serializer.data)


class AssetDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssetSerializer
    queryset = Asset.objects.all()
    

# Update api view to receive jwt token on each request
# https://github.com/tfranzel/drf-spectacular#customization-by-using-extend_schema
