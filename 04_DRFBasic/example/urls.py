from django.urls import path
from example.views import HelloAPI

urlpatterns = [
    path('hello/', HelloAPI),
]
