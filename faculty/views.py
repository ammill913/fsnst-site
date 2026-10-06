from django.shortcuts import render
from .models import Department, HomeContent, Program, ExchangeProgram

def home(request):
    content = HomeContent.objects.first()
    return render(request, "faculty/home.html", {"content": content})

def program_list(request):
    programs = Program.objects.select_related("department").all()
    return render(request, "faculty/program_list.html", {"programs": programs})

def department_list(request):
    departments = Department.objects.prefetch_related("programs").all()
    return render(request, "faculty/department_list.html", {"departments": departments})

def program_detail(request, program_id):
    program = Program.objects.select_related("department").get(id=program_id)
    disciplines_list = [
        d.strip() for d in program.disciplines.split("\n") if d.strip()
    ]
    return render(request, "faculty/program_detail.html", {"program": program, "disciplines": disciplines_list})

def department_detail(request, department_id):
    department = Department.objects.prefetch_related("programs", "teachers").get(id=department_id)
    return render(request, "faculty/department_detail.html", {"department": department})

def exchange_list(request):
    programs = ExchangeProgram.objects.all()
    return render(request, "faculty/exchange_list.html", {"programs": programs})
