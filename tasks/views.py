from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from employees.models import Employee
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def task_list(request):

    # Current logged-in user ke employees ke tasks hi fetch honge
    tasks = Task.objects.select_related("employee").filter(
        employee__user=request.user
    )
    
    search = request.GET.get("search", "")

    if search:
        tasks = tasks.filter(
            employee__name__icontains=search
        )

    paginator = Paginator(tasks, 5)

    page = request.GET.get("page")

    tasks = paginator.get_page(page)

    total_tasks = Task.objects.filter(
        employee__user=request.user
    ).count()

    completed = Task.objects.filter(
        employee__user=request.user,
        status="Completed"
    ).count()

    pending = Task.objects.filter(
        employee__user=request.user,
        status="Pending"
    ).count()

    in_progress = Task.objects.filter(
        employee__user=request.user,
        status="In Progress"
    ).count()

    context = {
        "tasks": tasks,
        "total_tasks": total_tasks,
        "completed": completed,
        "pending": pending,
        "in_progress": in_progress,
    }

    return render(request, "task_list.html", context)

@login_required
def add_task(request):
    employees = Employee.objects.filter(
        user=request.user
    )

    if request.method == "POST":

        employee = get_object_or_404(
            Employee,
            id=request.POST["employee"],
            user=request.user
        )

        Task.objects.create(
            employee=employee,
            title=request.POST["title"],
            description=request.POST["description"],
            priority=request.POST["priority"],
            status=request.POST["status"],
        )

        messages.success(
            request,
            "Task Added Successfully."
        )

        return redirect("task_list")

    return render(
        request,
        "add_task.html",
        {
            "employees": employees
        }
    )

@login_required
def view_task(request, id):
    task = get_object_or_404(Task, id=id,employee__user=request.user)

    context = {
        "task": task
    }

    return render(request, "view_task.html", context)

@login_required
def edit_task(request, id):
    task = get_object_or_404(
        Task,
        id=id,
        employee__user=request.user
    )

    employees = Employee.objects.filter(
        user=request.user
    )

    if request.method == "POST":

        employee = get_object_or_404(
            Employee,
            id=request.POST["employee"],
            user=request.user
        )

        task.employee = employee
        task.title = request.POST["title"]
        task.description = request.POST["description"]
        task.priority = request.POST["priority"]
        task.status = request.POST["status"]

        task.save()

        messages.success(
            request,
            "Task updated successfully."
        )

        return redirect("task_list")

    context = {
        "task": task,
        "employees": employees,
    }

    return render(
        request,
        "edit_task.html",
        context
    )

@login_required
def delete_task(request, id):
    task = get_object_or_404(
        Task,
        id=id,
        employee__user=request.user
    )

    if request.method == "POST":

        task.delete()

        messages.success(
            request,
            "Task deleted successfully."
        )

        return redirect("task_list")

    context = {
        "task": task
    }

    return render(
        request,
        "delete_task.html",
        context
    )