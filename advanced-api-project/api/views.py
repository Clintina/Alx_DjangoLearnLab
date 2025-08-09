from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.exceptions import NotFound
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """
    GET /api/books/
    List all books. Public read-only access.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookDetailView(generics.RetrieveAPIView):
    """
    GET /api/books/<int:pk>/
    Retrieve book details. Public read-only access.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    """
    POST /api/books/create/
    Create a new book. Authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class BookUpdateView(generics.UpdateAPIView):
    """
    PUT/PATCH /api/books/update/?pk=<id>
    Update an existing book. Authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        pk = self.request.query_params.get('pk') or self.request.data.get('id')
        if not pk:
            raise NotFound(detail="Book ID (pk) not provided.")
        return generics.get_object_or_404(Book, pk=pk)

    def perform_update(self, serializer):
        serializer.save()

class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE /api/books/delete/?pk=<id>
    Delete a book by ID. Authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        pk = self.request.query_params.get('pk') or self.request.data.get('id')
        if not pk:
            raise NotFound(detail="Book ID (pk) not provided.")
        return generics.get_object_or_404(Book, pk=pk)
