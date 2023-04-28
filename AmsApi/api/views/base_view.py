from typing import Tuple, Type, TypeVar

from django.db.models import Model
from django.http import HttpRequest, JsonResponse
from rest_framework import permissions, serializers, status, views
from rest_framework.response import Response

M = TypeVar("M", bound=Model)
S = TypeVar("S", bound=serializers.ModelSerializer)
P = Tuple[permissions.BasePermission, ...]


class BaseView(views.APIView):
    serializer: Type[S]
    model: Type[M]
    permission_classes = Type[P]

    def post(self, request: HttpRequest):
        serializer = self.serializer(
            data=request.data, context={"request": self.request}
        )

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, safe=False)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, _request, id=None):
        if id is not None:
            try:
                model_instance = self.model.objects.get(id=id)
                data = self.serializer(instance=model_instance).data
                response = JsonResponse(data=data)
            except self.model.DoesNotExist:
                response = JsonResponse(
                    {"status_code": 404, "error": "The resource was not found"},
                    status=404,
                )
        else:
            model_instance = self.model.objects.all()
            data = self.serializer(instance=model_instance, many=True).data
            response = JsonResponse(data=data, safe=False)

        return response

    def delete(self, _request, id):
        try:
            model_instance = self.model.objects.get(id=id)
            model_instance.delete()
            response = Response(None, status=status.HTTP_200_OK)
        except self.model.DoesNotExist:
            response = JsonResponse(
                {"status_code": 404, "error": "The resource was not found"},
                status=404,
            )

        return response
