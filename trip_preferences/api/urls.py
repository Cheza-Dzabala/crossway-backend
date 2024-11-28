from django.urls import path
from .views import TripPreferencesAPI

urlpatterns = [
	path('', TripPreferencesAPI.as_view()),
]