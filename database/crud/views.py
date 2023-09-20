from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Employee

# Create your views here.

def home(request):
    context = {'name': 'Admin'}
    return render(request, 'home.html', context)


# Create /Insert
def insert_emp(request):
    if request.method == "POST":
        eid = request.POST.get("eid")
        ename = request.POST.get("ename")
        email = request.POST.get("email")
        emp = Employee.objects.create(empid=eid, empname=ename, email=email)
        emp.save()
        return redirect('/')
    return render(request, 'insert.html')


# Retrieve ALL
def display_all(request):
    emp = Employee.objects.all()
    context = {'employees': emp}
    return render(request, 'display.html', context)


# UPDATE
def update_emp(request, id):
    emp = Employee.objects.get(empid=id)
    if request.method=="POST":
        emp.empid=request.POST.get("eid")
        emp.empname = request.POST.get("ename")
        emp.email = request.POST.get("email")
        emp.save()
        return redirect("/displayall/")
    return render(request, 'update.html', {'employee': emp})


def delete_emp(request,id):
    emp = Employee.objects.get(empid=id)
    if request.method=="POST":
        emp.delete()
        return redirect("/displayall/")
    return render(request,'delete.html',{'employee':emp})

