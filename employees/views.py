from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Manager, Intern
from .serializers import ManagerSerializer, InternSerializer

class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

    @action(detail=True, methods=['get'])
    def role(self, request, pk=None):
        manager = self.get_object()
        return Response({"role": manager.get_role()})

class InternViewSet(viewsets.ModelViewSet):
    queryset = Intern.objects.all()
    serializer_class = InternSerializer

    @action(detail=True, methods=['get'])
    def role(self, request, pk=None):
        intern = self.get_object()
        return Response({"role": intern.get_role()})

