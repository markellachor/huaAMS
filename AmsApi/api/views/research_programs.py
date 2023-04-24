from api.models import ResearchProgram
from django.http import JsonResponse
from rest_framework import permissions, status, views
from rest_framework.response import Response

from . import serializers


class ResearchProgramsView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = serializers.ResearchProgramSerializer(
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
                research_program_instance = ResearchProgram.objects.get(id=id)
                data = serializers.ResearchProgramSerializer(
                    instance=research_program_instance
                ).data
                response = JsonResponse(data=data)
            else:
                research_program_instance = ResearchProgram.objects.all()
                data = serializers.ResearchProgramSerializer(
                    instance=research_program_instance, many=True
                ).data
                response = JsonResponse(data=data, safe=False)
        except ResearchProgram.DoesNotExist:
            response = JsonResponse(
                {"status_code": 404, "error": "The resource was not found"}, status=404
            )

        return response

    def delete(self, _request, id):
        try:
            research_program_instance = ResearchProgram.objects.get(id=id)
            research_program_instance.delete()
            response = Response(None, status=status.HTTP_200_OK)
        except ResearchProgram.DoesNotExist:
            response = JsonResponse(
                {"status_code": 404, "error": "The resource was not found"},
                status=404,
            )

        return response
