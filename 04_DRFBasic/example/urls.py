from django.urls import path
from example.views import helloAPI, HelloAPI

urlpatterns = [
    path('hello/fbv/', helloAPI),
    path('hello/cbv/', HelloAPI.as_view()),
]