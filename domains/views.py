from rest_framework import generics
from domains.models import Domain
from domains.serializers import DomainSerializer
from domains.permissions import CustomPermission
from rest_framework import permissions


class DomainList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, CustomPermission)
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer



class DomainDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomPermission,)
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer
