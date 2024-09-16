from django.shortcuts import render
from django.views import View
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import QuickTips, Trip
from .serializers import QuickTipsSerializer, TripSerializer


class QuickTipsListView(generics.ListAPIView):
    queryset = QuickTips.objects.all().order_by('-posted_at')
    serializer_class = QuickTipsSerializer


class QuickTipsCreateView(generics.CreateAPIView):
    queryset = QuickTips.objects.all()
    serializer_class = QuickTipsSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)


class TripCreateApiView(generics.CreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TripListApiView(generics.ListAPIView):
    serializer_class = TripSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Trip.objects.filter(user=self.request.user)
