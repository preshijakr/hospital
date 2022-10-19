from django.shortcuts import render

# Create your views here.
def doctors(request):
    return render(request, 'employees/doctors.html')

def staff_nurse(request):
    return render(request, 'employees/staff_nurse.html')

def attender(request):
    return render(request,'employees/attender.html')
