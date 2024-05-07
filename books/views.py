from rest_framework import generics
from .models import Book, Wishlist, ReadingHistory
from .serializers import BookSerializer, WishlistSerializer, ReadingHistorySerializer

class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class WishlistListCreate(generics.ListCreateAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class ReadingHistoryListCreate(generics.ListCreateAPIView):
    queryset = ReadingHistory.objects.all()
    serializer_class = ReadingHistorySerializer

class BookListByGenre(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        genre = self.kwargs['genre']
        return Book.objects.filter(genre=genre)
