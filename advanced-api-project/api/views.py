from rest_framework import generics, permissions
from rest_framework.exceptions import NotFound
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """
    GET /api/books/
    List all books. Public access.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class BookDetailView(generics.RetrieveAPIView):
    """
    GET /api/books/<int:pk>/
    Retrieve a single book by ID. Public access.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class BookCreateView(generics.CreateAPIView):
    """
    POST /api/books/create/
    Create a new book. Authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class BookUpdateView(generics.UpdateAPIView):
    """
    PUT/PATCH /api/books/update/?pk=<id>
    Update an existing book by ID passed as query param or in request data.
    Authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        pk = self.request.query_params.get('pk') or self.request.data.get('id')
        if not pk:
            raise NotFound(detail="Book ID (pk) not provided in query parameters or request data.")
        return generics.get_object_or_404(Book, pk=pk)

    def perform_update(self, serializer):
        serializer.save()

class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE /api/books/delete/?pk=<id>
    Delete a book by ID passed as query param or in request data.
    Authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        pk = self.request.query_params.get('pk') or self.request.data.get('id')
        if not pk:
            raise NotFound(detail="Book ID (pk) not provided in query parameters or request data.")
        return generics.get_object_or_404(Book, pk=pk)
