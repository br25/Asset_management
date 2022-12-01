from rest_framework import generics, status, views, permissions

from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

from .models import Employee
from .serializers import EmployeeSerializer
from .permissions import IsCompanyEmployee

# class EmployeeView(generics.GenericAPIView):

#     serializer_class = EmployeeSerializer
#     # renderer_classes = (UserRenderer,)

#     def post(self, request):
#         employee = request.data
#         serializer = self.serializer_class(data=employee)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         user_data = serializer.data
#         return Response(user_data, status=status.HTTP_201_CREATED)


class EmployeeList(generics.ListCreateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]


    # def get(self, request, *args, **kwargs):
    #     queryset = Employee.objects.all()
    #     print(queryset)
    #     serializer = EmployeeSerializer(queryset)
    #     return Response(serializer.data)


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()