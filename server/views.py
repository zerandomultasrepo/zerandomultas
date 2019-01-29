from rest_framework import viewsets
from server.serializers import OccurrenceSerializer
from server.models import Occurrence

from rest_framework.permissions import BasePermission, IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.views import ObtainJSONWebToken


SAFE_METHODS = ('POST', 'HEAD', 'OPTIONS', 'GET')


class IsAuthenticatedOrCreate(BasePermission):
    """
    The request is authenticated as a user, or is a create request.
    """

    def has_permission(self, request, view):
        return (
                request.method in SAFE_METHODS or
                request.user and
                request.user.is_authenticated()
        )


class LoginView(ObtainJSONWebToken):
    """
    Allow the user login in system
    """


class OccurrenceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Occurrence.objects.all()
    serializer_class = OccurrenceSerializer
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticatedOrCreate,)
