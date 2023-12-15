from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_book , name='book-list-create'),
    path('add_book', views.post_book, name='book-list-add'),
]
