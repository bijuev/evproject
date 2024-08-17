from django.shortcuts import render
from django.views import View
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from elasticsearch_dsl.query import MultiMatch, Bool, Wildcard

from .documents import QuickTipsDocument
from .models import QuickTips, Trip
from .serializers import QuickTipsSerializer, TripSerializer


class QuickTipsSearchHtmlView(View):
    def get(self, request):
        query = request.GET.get('q', '')
        search_results = []
        if query:
            multi_match_query = MultiMatch(
                query=query,
                fields=["title^3", "content"],
                type="best_fields",
                fuzziness="AUTO"
            )
            wildcard_query = Bool(should=[
                Wildcard(title={"value": f"*{query}*", "boost": 2}),
                Wildcard(content={"value": f"*{query}*"})
            ])
            combined_query = Bool(should=[multi_match_query, wildcard_query])
            search = QuickTipsDocument.search().query(combined_query)
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
