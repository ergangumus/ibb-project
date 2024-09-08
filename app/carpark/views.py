from rest_framework import viewsets
from .models import CarPark
from .serializers import CarParkSerializer
from .permissions import IsSuperUserOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, authentication, permissions


class CarParkViewSet(viewsets.ModelViewSet):
    queryset = CarPark.objects.all()
    serializer_class = CarParkSerializer

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsSuperUserOrReadOnly]
