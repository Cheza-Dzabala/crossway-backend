from django.urls import path
from .views import DriverApi

urlpatterns = [
	path('', DriverApi.as_view()),
]