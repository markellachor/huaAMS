from api.models import Building
from django.http import JsonResponse
from rest_framework import permissions, status, views
from rest_framework.response import Response

from . import serializers


class BuildingsView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = serializers.BuildingSerializer(
            data=request.data, context={"request": self.request}
        )

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, safe=False)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, _request, id=None):
        try:
            if id is not None:
                building_instance = Building.objects.get(id=id)
                data = serializers.BuildingSerializer(instance=building_instance).data
                response = JsonResponse(data=data)
            else:
                building_instance = Building.objects.all()
                data = serializers.BuildingSerializer(
                    instance=building_instance, many=True
                ).data
                response = JsonResponse(data=data, safe=False)
        except Building.DoesNotExist:
            response = JsonResponse(
                {"status_code": 404, "error": "The resource was not found"}, status=404
            )

        return response

    def delete(self, _request, id):
        try:
            building_instance = Building.objects.get(id=id)
            building_instance.delete()
            response = Response(None, status=status.HTTP_200_OK)
        except Building.DoesNotExist:
            response = JsonResponse(
                {"status_code": 404, "error": "The resource was not found"},
                status=404,
            )

        return response
