from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse  # Import HttpResponse
from .models import Emp

# Create your views here.


def emp_home(request):
    emps = Emp.objects.all()
    return render(request, "emp/Home.html", {"emps": emps})  # Return a valid response


def emp_add(request):
    if request.method == "POST":
        print("Add Employee")
        emp_id = request.POST.get("emp_id")
        emp_name = request.POST.get("emp_name")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_working = request.POST.get("emp_working")
        emp_department = request.POST.get("emp_department")
        e = Emp()
        e.name = emp_name
        e.emp_id = emp_id
        e.phone = emp_phone
        e.address = emp_address
        e.department = emp_department

        if emp_working is None:
            e.working = False
        else:
            e.working = True

        e.save()

        return redirect("/emp/Home/")
    return render(request, "emp/emp_Add.html", {})

def emp_delete(request,emp_id):
     emp = get_object_or_404(Emp, pk=emp_id)
     emp.delete()
     return redirect("/emp/Home/")


def emp_updated(request,emp_id):
    emp = get_object_or_404(Emp, pk=emp_id)
    return render(request,"emp/updated_emp.html",{"emp":emp})


def to_Updated(request,emp_id):
     if request.method == "POST":
        print("Add Employee")
        emp_id_temp = request.POST.get("emp_id")
        emp_name = request.POST.get("emp_name")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_working = request.POST.get("emp_working")
        emp_department = request.POST.get("emp_department")
        e = get_object_or_404(Emp, pk=emp_id)
        e.name = emp_name
        e.emp_id = emp_id_temp
        e.phone = emp_phone
        e.address = emp_address
        e.department = emp_department

        if emp_working is None:
            e.working = False
        else:
            e.working = True
        
        e.save()
   
        return redirect("/emp/Home/")
    
    
    
def Testimonial(request):
    return HttpResponse("adjskljslak")