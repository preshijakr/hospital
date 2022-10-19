from django.urls import path
from . import views
urlpatterns = [
   
    path('doctors', views.doctors),
    path('nurse', views.staff_nurse),
    path('attender', views.attender)
    
]