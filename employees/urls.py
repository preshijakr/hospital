from django.urls import path

urlpatterns = [
   
    path('doctors', views.doctors),
    path('nurse', views.staff-nurse),
    path('attender', views.attender)
    
]