from django.urls import path
from example.views import helloAPI, bookAPI, booksAPI, HelloAPI, BookAPI, BooksAPI, BookAPIMixins, BooksAPIMixins, BookAPIGenerics, BooksAPIGenerics

urlpatterns = [
    path('fbv/hello/', helloAPI),
    path('fbv/books/', booksAPI),
    path('fbv/book/<int:bid>/', bookAPI),
    path('cbv/hello/', HelloAPI.as_view()),
    path('cbv/books/', BooksAPI.as_view()),
    path('cbv/book/<int:bid>/', BookAPI.as_view()),
    path('mixin/books/', BooksAPIMixins.as_view()),
    path('mixin/book/<int:bid>/', BookAPIMixins.as_view()),
    path('generics/books/', BooksAPIGenerics.as_view()),
    path('generics/book/<int:bid>/', BookAPIGenerics.as_view()),
]