from api.views.base_view import BaseView
from django.contrib.auth import get_user_model
from rest_framework import permissions, serializers, status, views
from django.http import HttpRequest, JsonResponse
from rest_framework.response import Response
from api.models import Profile

from .. import serializers

UserModel = get_user_model()


class UsersView(BaseView):
    serializer = serializers.UserSerializer
    # TODO: Staff or admin?
    permission_classes = (permissions.IsAdminUser,)
    model = UserModel

    def post(self, request: HttpRequest):
        profile_data = request.data.pop('profile')
        user_data = request.data
        
        user_serializer = self.serializer(
            data=user_data, context={"request": self.request}
        )

        if user_serializer.is_valid():
            user_serializer.save()
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        profile_data["user"] = user_serializer.data.get('id')
        profile_serializer = serializers.ProfileSerializer(
            data=profile_data, context={"request": self.request}
        )

        if profile_serializer.is_valid():
            profile_serializer.save()
            user = self.model.objects.get(id=user_serializer.data.get('id'))
            data = self.serializer(instance=user).data
            return JsonResponse(data=data, safe=False)
        else:
            return Response(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request: HttpRequest, id):
        profile_data = request.data.pop('profile')

        user_instance = self.model.objects.get(id=id)
        user_serializer = self.serializer(
            user_instance,
            data=request.data,
            partial=True,
            context={"request": self.request},
        )

        if user_serializer.is_valid():
            user_serializer.save()
        else:
            response = Response(
                user_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
        
        if profile_data is None or len(profile_data) == 0:
            user = self.model.objects.get(id=user_instance.id)
            data = self.serializer(instance=user).data
            return JsonResponse(data=data, safe=False)
 
        profile_data["user"] = user_instance.id
        try:
            profile_instance = Profile.objects.get(user_id=user_instance.id)
            serializer = serializers.ProfileSerializer(
                profile_instance,
                data=profile_data,
                partial=True,
                context={"request": self.request},
            )

            if serializer.is_valid():
                serializer.save()
            else:
                return Response(
                    serializer.errors, status=status.HTTP_400_BAD_REQUEST
                )
        except Profile.DoesNotExist:
            profile_serializer = serializers.ProfileSerializer(
                data=profile_data, context={"request": self.request}
            )
            if profile_serializer.is_valid():
                profile_serializer.save()
            else:
                return Response(
                    profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST
                )
        user = self.model.objects.get(id=user_instance.id)
        data = self.serializer(instance=user).data
        return JsonResponse(data=data, safe=False)
