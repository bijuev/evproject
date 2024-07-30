from django.shortcuts import render
from django.views import View
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .documents import QuickTipsDocument
from .models import QuickTips, Trip
from .serializers import QuickTipsSerializer, TripSerializer


class QuickTipsSearchHtmlView(View):
    def get(self, request):
        query = request.GET.get('q', '')
        search_results = []
        if query:
            search = QuickTipsDocument.search().query(
                "bool",
                should=[
                    {"match": {"title": {"query": query, "fuzziness": "AUTO"}}},
                    {"match": {"content": {"query": query, "fuzziness": "AUTO"}}},
                    {"match_phrase_prefix": {"title": query}},
                    {"match_phrase_prefix": {"content": query}}
                ],
                minimum_should_match=1
            )
            search_results = search.to_queryset()
        return render(request, 'quicktips_search.html', {'search_results': search_results, 'query': query})


class QuickTipsSearchView(APIView):
    def get(self, request):
        query = request.query_params.get('q', None)
        if query:
            search = QuickTipsDocument.search().query("match", content={
                "query": query,
                "fuzziness": "AUTO"
            })
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
