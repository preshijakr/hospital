from django.shortcuts import render

# Create your views here.
def doctors(request):
    return render(request, 'doctors.html')

def staff-nurse(request):
    return render(request, 'staff-nurse.html')

def attender(request):
    return render(request, attender.html)
