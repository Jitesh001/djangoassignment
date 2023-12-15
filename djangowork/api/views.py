from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Book
from .serializers import BookSerializer

# @api_view(['GET'])
# def get_book(request):
#     books = Book.objects.all()
#     serializer = BookSerializer(books, many=True)
#     return Response({'status':200, 'payload':serializer.data})

# @api_view(['POST'])
# def post_book(request):
#     book_data = request.data
#     serializer = BookSerializer(data = request.data)
    
#     if not serializer.is_valid():
#         print(serializer.errors)
#         return Response({'status':403, 'errors':serializer.errors, 'message':'somehting went wrong'})
    
#     serializer.save()

#     return Response({'status':200, 'payload':serializer.data, 'message':'data sent successfully!'})
