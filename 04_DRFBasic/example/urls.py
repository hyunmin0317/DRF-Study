from django.urls import path
from example.views import HelloAPI, booksAPI, bookAPI, BooksAPI, BookAPI, helloAPI

urlpatterns = [
    path("fbv/hello/", helloAPI),
    path("fbv/books/", booksAPI),
    path("fbv/book/<int:bid>/", bookAPI),
    path("cbv/hello/", HelloAPI.as_view()),
    path("cbv/books/", BooksAPI.as_view()),
    path("cbv/book/<int:bid>/", BookAPI.as_view()),
]
