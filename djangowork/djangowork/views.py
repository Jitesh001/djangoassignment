from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from api.models import Book
from api.serializers import BookSerializer

def hello_view(request):
    return HttpResponse("Hello, Django!")

class BookAPI(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response({'status':200, 'payload':serializer.data})

    def post(self, request):
        data = request.data
        serializer = BookSerializer(data = request.data)
        
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status':403, 'errors':serializer.errors, 'message':'somehting went wrong'})
        
        serializer.save()

        return Response({'status':200, 'payload':serializer.data, 'message':'data sent successfully!'})


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validate_user):
        user = User.objects.create(username = validate_user['username'])
        user.set_password(validate_user['username'])
        user.save()
        return user

class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({'status':403, 'errors':serializer.errors, 'message':'somehting went wrong'})
        
        serializer.save()

        user = User.objects.get(username=serializer.data['username'])
        token, _ = Token.objects.get_or_create(user=user)
        
        return Response({'status':200, 'payload':serializer.data, 'token':str(token)})