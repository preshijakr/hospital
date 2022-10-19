from django.urls import path
from . import views

urlpatterns = [
    path('departmrnt', views.department),
    path('patient_profile', views.patient_profile)
]
