from rest_framework import generics
from books.models import Book
from .serializars import BookSerializer
from .permissions import IsAuthorOrReadOnly

class BookAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    
class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly)
    queryset = Book.objects.all()
    serializer_class = BookSerializer