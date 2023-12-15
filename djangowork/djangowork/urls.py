from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework.authtoken import views

urlpatterns = [
    path('index/', hello_view, name='hello_view'),
    path('admin/', admin.site.urls),
    # path('books', include('api.urls')),
    path('books', BookAPI.as_view()),
    path('register_token', RegisterUser.as_view()),
]

