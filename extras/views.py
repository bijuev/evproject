from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Trip, QuickTips
from .serializers import TripSerializer, QuickTipsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .documents import QuickTipsDocument


class QuickTipsSearchView(APIView):
    def get(self, request):
        query = request.query_params.get('q', None)
        if query:
            search = QuickTipsDocument.search().query("match", content=query)
            results = search.execute()
            serializer = QuickTipsSerializer(results.hits, many=True)
            return Response(serializer.data)
        return Response([])


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
