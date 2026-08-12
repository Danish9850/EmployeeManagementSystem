from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Leave
from employees.models import Employee
from django.core.paginator import Paginator
# Create your views here.

@login_required
def apply_leave(request):
    employees = Employee.objects.all()
    if request.method == "POST":
        employee_id = request.POST.get("employee")
        leave_type = request.POST.get("leave_type")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        reason = request.POST.get("reason")

        employee = Employee.objects.get(id=employee_id)

        Leave.objects.create(
            employee=employee,
            leave_type=leave_type,
            start_date=start_date,
            end_date=end_date,
            reason=reason,
            status="Pending"
        )

        messages.success(request,"Leave Applied Successfully.")
        return redirect("leave_list")

    context = {
        "employees":employees,
        "total_employees":employees.count(),
    }

    return render(request,"apply_leave.html", context)

@login_required
def leave_list(request):
    search = request.GET.get("search")

    leaves = Leave.objects.select_related("employee").all()

    if search:
        leaves = leaves.filter(employee__name__icontains=search)

    # Pagination hamesha chalegi
    paginator = Paginator(leaves, 5)
    page = request.GET.get("page")
    leaves = paginator.get_page(page)

    context = {
        "leaves": leaves,
        "total_leaves": Leave.objects.count(),
        "approved": Leave.objects.filter(status="Approved").count(),
        "pending": Leave.objects.filter(status="Pending").count(),
        "rejected": Leave.objects.filter(status="Rejected").count(),
    }

    return render(request, "leave_list.html", context)

@login_required
def leave_detail(request, id):
    leave = Leave.objects.get(id=id)

    context = {
        "leave":leave
    }

    return render(request,"leave_detail.html", context)

@login_required
def approve_leave(request, leave_id):
    leave = get_object_or_404(Leave, id=leave_id)
    leave.status = "Approved"
    leave.save()
    messages.success(request, "Leave Approved Successfully.")
    return redirect("leave_list")

@login_required
def reject_leave(request, leave_id):
    leave = get_object_or_404(Leave, id=leave_id)
    leave.status = "Rejected"
    leave.save()
    messages.success(request, "Leave Rejected Successfully.")
    return redirect("leave_list")

@login_required
def edit_leave(request, id):
    leave = get_object_or_404(Leave, id=id)
    employees = Employee.objects.all()
    if request.method == "POST":
        leave.employee_id = request.POST.get("employee")
        leave.leave_type = request.POST.get("leave_type")
        leave.start_date = request.POST.get("start_date")
        leave.end_date = request.POST.get("end_date")
        leave.reason = request.POST.get("reason")
        leave.save()
        messages.success(
            request,"Leave Updated Successfully."
        )

        return redirect("leave_list")

    context = {
        "leave":leave,
        "employees": Employee.objects.all(),
        "total_employees":Employee.objects.count(),
    }

    return render(request, "edit_leave.html", context)

