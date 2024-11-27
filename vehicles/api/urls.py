from django.urls import path
from . import views

urlpatterns = [
	path('', views.VehiclesAPI.as_view()),
]