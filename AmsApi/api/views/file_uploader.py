from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from api.models import File

from . import serializers


class FileUploadAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer = serializers.FileUploadSerializer
    
    def post(self, request):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, safe=False)
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def get(self, _, id):
        try:
            model_instance = File.objects.get(id=id)
            data = self.serializer(instance=model_instance).data
            response = JsonResponse(data=data)
        except File.DoesNotExist:
            response = JsonResponse(
                {"status_code": 404, "error": "The resource was not found"},
                status=404,
            )

        return response