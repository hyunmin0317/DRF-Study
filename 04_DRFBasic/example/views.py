from django.shortcuts import get_object_or_404
from rest_framework import status, mixins, generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from example.models import Book
from example.serializers import BookSerializer


# FBV
@api_view(['GET'])
def helloAPI(request):
    return Response("hello world!")


@api_view(['GET', 'POST'])
def booksAPI(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def bookAPI(request, bid):
    book = get_object_or_404(Book, bid=bid)
    serializer = BookSerializer(book)
    return Response(serializer.data, status=status.HTTP_200_OK)


# CBV
class HelloAPI(APIView):
    def get(self, request):
        return Response("hello world")


class BooksAPI(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookAPI(APIView):
    def get(self, request, bid):
        book = get_object_or_404(Book, bid=bid)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)


# DRF mixins
class BooksAPIMixins(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):  # ListModelMixin
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):  # CreateModelMixin
        return self.create(request, *args, **kwargs)


class BookAPIMixins(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'bid'

    def get(self, request, *args, **kwargs):  # RetrieveModelMixin
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):  # UpdateModelMixin
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):  # DestroyModelMixin
        return self.destroy(request, *args, **kwargs)


# DRF generics
class BooksAPIGenerics(generics.ListCreateAPIView):     # ListModelMixin, CreateModelMixin
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookAPIGenerics(generics.RetrieveUpdateDestroyAPIView):     # RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'bid'

# 5가지 메인 기능: ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
# 4가지 조합 기능: ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView


# DRF Viewset
class BookViewSet(viewsets.ModelViewSet):       # ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
    queryset = Book.objects.all()
    serializer_class = BookSerializer
