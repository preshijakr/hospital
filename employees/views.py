from django.shortcuts import render

# Create your views here.
def doctors(request):
    return render(request, 'doctors.html')

def staff_nurse(request):
    return render(request, 'staff_nurse.html')

def attender(request):
    return render(request, attender.html)
