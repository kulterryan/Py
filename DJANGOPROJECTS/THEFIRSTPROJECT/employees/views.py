from THEFIRSTPROJECT import employees
from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Employeer
# Create your views here.
def home(request):
    employees = Employeer.object.all()
    return render(request, 'home.html', {'employees': employees})

def employee_detail(request, employee_id):
    try:
        employee = Employeer.objects.get(employee_id=employee_id)
    except Employeer.DoesNotExist:
        raise Http404("Employee Not Found")
    return render(request, 'employee_detail.html', {'employee':employee})