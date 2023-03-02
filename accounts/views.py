from rest_framework import status
from .serializers import UserSerializer
from rest_framework import serializers
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate

class LoginView(APIView):

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            user_serializer = UserSerializer(user)
            return Response({"user": user_serializer.data,"message": "Login successful"})
        else:
            return Response({"error": "Invalid credentials"}, status=400)




# class LoginView(APIView):
#     authentication_classes = (BasicAuthentication)
#     permission_classes = (IsAuthenticated)

#     def post(self, request):
#         username = request.data.get("username")
#         password = request.data.get("password")
#         user = authenticate(username=username, password=password)
#         print(user)
#         if user is not None:
#             user_serializer = UserSerializer(user)
#             return Response({"message": "Login successful", "user": user_serializer.data})
#         else:
#             return Response({"error": "Invalid credentials"},
#                             status=status.HTTP_400_BAD_REQUEST)



