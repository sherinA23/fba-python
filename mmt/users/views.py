from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from .serializers import *
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from rest_framework.authentication import TokenAuthentication



# Create your views here.

# class UserRegistration():
#     model = get_user_model()
#     permission_classes = [permissions.AllowAny]
#     serializer_class = UsersSerializer

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view()
def index(request):
    return Response({"message": "Hello, world!"})

@api_view(['POST'])
def sign_up(request):
    try:
        data = request.data
        print(data)
    
        User = get_user_model()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        role = data.get('role')

        user = User.objects.create_user(username=username, email=email, password=password, role=role)
        return JsonResponse({'success': 'registered successfully'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

class UserLoginAPIView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                token, created = Token.objects.get_or_create(user=user)
                return Response({'message': 'Logged in successfully', 'token': token.key})
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class ProtectedAPIView(APIView):
    def get(self, request):
        return Response({'message': 'You are authenticated!'})
    
class LogoutAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Delete the user's token
        Token.objects.filter(user=request.user).delete()
        return Response({'detail': 'Logout successful'}, status=status.HTTP_200_OK)
    