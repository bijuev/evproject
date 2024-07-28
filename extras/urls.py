from django.urls import path
from .views import (TripCreateApiView, TripListApiView, QuickTipsListView, QuickTipsCreateView,
                    QuickTipsSearchView)

urlpatterns = [
    path('api/trips/create/', TripCreateApiView.as_view(), name='trip_create'),
    path('api/trips/', TripListApiView.as_view(), name='trip_list'),
    path('api/quick-tips/', QuickTipsListView.as_view(), name='quick_tips_list'),
    path('api/quick-tips/create/', QuickTipsCreateView.as_view(), name='quick_tips_create'),
    path('api/quick-tips/search/', QuickTipsSearchView.as_view(), name='quick_tips_search'),
]
