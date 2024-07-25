from multiprocessing import context
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render

from employeeapp.models import Employee

# Create your views here.

def display(request):
    employees = Employee.objects.all()
    print(employees)
    context = {
       "employees" : employees
    }
    return render(request, "home.html", context)


# def employee_details(request, id):
#     try:
#         employee = Employee.objects.get(id=id)
#         print(employee)
#     except:
#         raise Http404
    
#   ----------------------OR-----------------------


def employee_details(request, id):
    employee = get_object_or_404(Employee, id = id)
    context = {
        "employee" : employee
    }
    return render(request, "employee_details.html", context)
