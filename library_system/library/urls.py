from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookListCreate.as_view(), name='book-list'),
    path('books/<int:pk>/', views.BookDetail.as_view(), name='book-detail'),
    path('users/', views.UserListCreate.as_view(), name='user-list'),
    path('transactions/', views.TransactionListCreate.as_view(), name='transaction-list'),
]
