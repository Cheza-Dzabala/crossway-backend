from django.urls import path
from . import views

urlpatterns = [
	path('', views.RidesAPI.as_view()),
] 