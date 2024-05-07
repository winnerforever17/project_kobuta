from django.urls import path
from .views import (
    BookListCreate, BookRetrieveUpdateDestroy, WishlistListCreate,
    BookDetailView, ReadingHistoryListCreate, BookListByGenre
)

urlpatterns = [
    path('books/', BookListCreate.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroy.as_view(), name='book-detail'),
    path('wishlist/', WishlistListCreate.as_view(), name='wishlist-list-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail-view'),
    path('reading-history/', ReadingHistoryListCreate.as_view(), name='reading-history-list-create'),
    path('books/genre/<str:genre>/', BookListByGenre.as_view(), name='book-list-by-genre'),
]
