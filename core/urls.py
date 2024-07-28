from django.urls import path
from .views import LocationApiView, home, LocationCreateView, LocationCreateApiView, LocationUpdateApiView,\
    LocationDeleteApiView, LocationDetailApiView, LocationSearchApiView, LocationSearchCreateApiView, \
    login_view, logout_view, profile_view

urlpatterns = [
    path('api/location/', LocationApiView.as_view()),
    path('api/location/<int:pk>/', LocationDetailApiView.as_view()),
    path('api/location/add/', LocationCreateApiView.as_view()),
    path('api/location/<int:pk>/edit/', LocationUpdateApiView.as_view()),
    path('api/location/<int:pk>/delete/', LocationDeleteApiView.as_view()),

    path('api/location/search/', LocationSearchApiView.as_view()),
    path('api/location/search/add/', LocationSearchCreateApiView.as_view()),

    path('api/location/create/', LocationCreateView.as_view()),
    path('api/profile/', profile_view, name='api-profile'),
    path('api/login/', login_view, name='login'),
    path('api/logout/', logout_view, name='logout'),
    path('', home, name='home')
]
