from django.shortcuts import render, redirect
from rest_framework import generics
from django.contrib.auth import get_user_model
from django.views.generic import CreateView
from django.urls import reverse_lazy
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, logout
from .models import Location, LocationSearch, UserProfile
from .serializers import LocationSerializer, LocationSearchSerializer, UserProfileSerializer
from .forms import LocationForm

User = get_user_model()


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile_view(request):
    profile = request.user.profile
    serializer = UserProfileSerializer(profile)
    return Response(serializer.data)


class LocationSearchApiView(generics.ListAPIView):
    queryset = LocationSearch.objects.all()
    serializer_class = LocationSearchSerializer


class LocationSearchCreateApiView(generics.CreateAPIView):
    queryset = LocationSearch.objects.all()
    serializer_class = LocationSearchSerializer


class LocationApiView(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationDetailApiView(generics.RetrieveAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationCreateApiView(generics.CreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationUpdateApiView(generics.RetrieveUpdateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationDeleteApiView(generics.RetrieveDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return redirect('home')


class LocationCreateView(CreateView):
    model = Location
    form_class = LocationForm
    template_name = 'location_create.html'
    success_url = reverse_lazy('home')


def home(request):
    return render(request, 'index.html', {})


@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    else:
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    logout(request)
    return Response({'message': 'Logged out successfully'})
