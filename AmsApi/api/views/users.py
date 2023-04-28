from api.views.base_view import BaseView
from django.contrib.auth import get_user_model
from rest_framework import permissions

from . import serializers

UserModel = get_user_model()


class UsersView(BaseView):
    serializer = serializers.UserSerializer
    # TODO: Staff or admin?
    permission_classes = (permissions.IsAdminUser,)
    model = UserModel
