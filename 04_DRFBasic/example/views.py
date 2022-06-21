from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

@api_view(['GET'])
def HelloAPI(request):
    return Response("hello world!")


class HelloAPI(APIView):
    def get(self, request):
        return Response("hello world")