from django.shortcuts import render

# Create your views here.
def department(request):
    return render(request,department.html)

def patient_profile(request):
    return render(request,patient_profile.html)
