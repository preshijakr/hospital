from django.urls import path

urlpatterns = [
 
    path('home', include('employees.urls')),
  
]
