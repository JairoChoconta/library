
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Autor, Categoria, Editorial, Libro
from .serializers import AutorSerializer, CategoriaSerializer, EditorialSerializer, LibroSerializer

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class EditorialViewSet(viewsets.ModelViewSet):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

    @action(detail=False, methods=['get'], url_path='autor/(?P<autor_id>[^/.]+)')
    def libros_por_autor(self, request, autor_id=None):
        libros = self.queryset.filter(autor_id=autor_id)
        serializer = self.get_serializer(libros, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='categoria/(?P<categoria_id>[^/.]+)')
    def libros_por_categoria(self, request, categoria_id=None):
        libros = self.queryset.filter(categoria_id=categoria_id)
        serializer = self.get_serializer(libros, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='editorial/(?P<editorial_id>[^/.]+)')
    def libros_por_editorial(self, request, editorial_id=None):
        libros = self.queryset.filter(editorial_id=editorial_id)
        serializer = self.get_serializer(libros, many=True)
        return Response(serializer.data)
