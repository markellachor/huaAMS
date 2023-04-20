from api.models import Department
from django.http import JsonResponse
from rest_framework import permissions, status, views
from rest_framework.response import Response

from . import serializers


class DepartmentsView(views.APIView):
    # TODO: Staff or admin?
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = serializers.DepartmentSerializer(
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
                department = Department.objects.get(id=id)
                data = serializers.DepartmentSerializer(instance=department).data
                response = JsonResponse(data=data)
            except Department.DoesNotExist:
                response = JsonResponse(
                    {"status_code": 404, "error": "The resource was not found"},
                    status=404,
                )
        else:
            department = Department.objects.all()
            data = serializers.DepartmentSerializer(instance=department, many=True).data
            response = JsonResponse(data=data, safe=False)

        return response
