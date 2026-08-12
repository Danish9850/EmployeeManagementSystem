from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from employees.models import Employee
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def task_list(request):
    search = request.GET.get("search")

    tasks = Task.objects.select_related("employee").all()

    if search:
        tasks = tasks.filter(
            employee__name__icontains=search
        )

        paginator = Paginator(tasks,5)
        page = request.GET.get("page")
        tasks = paginator.get_page(page)

    context = {
            "tasks": tasks,
            "total_tasks": Task.objects.count(),
            "completed": Task.objects.filter(status="Completed").count(),
            "pending": Task.objects.filter(status="Pending").count(),
            "in_progress": Task.objects.filter(status="In Progress").count(),
        }
    return render(request, "task_list.html", context)

def add_task(request):
    employees = Employee.objects.all()
    if request.method == "POST":
        employee = Employee.objects.get(id=request.POST["employee"])
        Task.objects.create(
            employee=employee,
            title=request.POST["title"],

            description=request.POST["description"],
            priority=request.POST["priority"],
            status=request.POST["status"],
        )

        messages.success(request, "Task Added Successfully.")

        return redirect("task_list")
    return render(request, "add_task.html",{
        "employees":employees
    })

def view_task(request, id):
    task = get_object_or_404(Task, id=id)

    context = {
        "task": task
    }

    return render(request, "view_task.html", context)

def edit_task(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == "POST":
        task.employee_id = request.POST["employee"]
        task.title = request.POST["title"]
        task.description = request.POST["description"]
        task.priority = request.POST["priority"]
        task.status = request.POST["status"]

        task.save()

        return redirect("task_list")

    context = {
        "task":task,
        "employees":Employee.objects.all(),
    }

    return render(request, "edit_task.html", context)

def delete_task(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == "POST":
        task.delete()
        return redirect("task_list")

    context = {
        "task":task
    }

    return render(request, "delete_task.html", context)
