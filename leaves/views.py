from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Leave
from employees.models import Employee
from django.core.paginator import Paginator
# Create your views here.

@login_required
def apply_leave(request):
    employees = Employee.objects.filter(
        user=request.user
    )

    if request.method == "POST":

        employee_id = request.POST.get("employee")
        leave_type = request.POST.get("leave_type")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        reason = request.POST.get("reason")

        employee = get_object_or_404(
            Employee,
            id=employee_id,
            user=request.user
        )

        Leave.objects.create(
            employee=employee,
            leave_type=leave_type,
            start_date=start_date,
            end_date=end_date,
            reason=reason,
            status="Pending"
        )

        messages.success(
            request,
            "Leave Applied Successfully."
        )

        return redirect("leave_list")

    context = {
        "employees": employees,
        "total_employees": employees.count(),
    }

    return render(
        request,
        "apply_leave.html",
        context
    )

@login_required
def leave_list(request):
    leaves = Leave.objects.select_related("employee").filter(
        employee__user=request.user
    )

    search = request.GET.get("search", "")

    if search:
        leaves = leaves.filter(
            employee__name__icontains=search
        )
    paginator = Paginator(leaves, 5)

    page = request.GET.get("page")

    leaves = paginator.get_page(page)
    user_leaves = Leave.objects.filter(
        employee__user=request.user
    )

    total_leaves = user_leaves.count()

    approved = user_leaves.filter(
        status="Approved"
    ).count()

    pending = user_leaves.filter(
        status="Pending"
    ).count()

    rejected = user_leaves.filter(
        status="Rejected"
    ).count()

    context = {
        "leaves": leaves,
        "total_leaves": total_leaves,
        "approved": approved,
        "pending": pending,
        "rejected": rejected,
    }

    return render(
        request,
        "leave_list.html",
        context
    )
@login_required
def leave_detail(request, id):
    leave = get_object_or_404(Leave,id=id,employee__user=request.user)

    context = {
        "leave":leave
    }
    return render(request,"leave_detail.html", context)

@login_required
def approve_leave(request, leave_id):
    leave = get_object_or_404(
        Leave,
        id=leave_id,
        employee__user=request.user
    )
    leave.status = "Approved"
    leave.save()
    messages.success(
        request,
        "Leave Approved Successfully."
    )
    return redirect("leave_list")

@login_required
def reject_leave(request, leave_id):
    leave = get_object_or_404(Leave, id=leave_id,employee__user=request.user)
    leave.status = "Rejected"
    leave.save()
    messages.success(request, "Leave Rejected Successfully.")
    return redirect("leave_list")

@login_required
def edit_leave(request, id):
    leave = get_object_or_404(
        Leave,
        id=id,
        employee__user=request.user
    )
    employees = Employee.objects.filter(
        user=request.user
    )

    if request.method == "POST":
        employee = get_object_or_404(
            Employee,
            id=request.POST.get("employee"),
            user=request.user
        )

        leave.employee = employee
        leave.leave_type = request.POST.get("leave_type")
        leave.start_date = request.POST.get("start_date")
        leave.end_date = request.POST.get("end_date")
        leave.reason = request.POST.get("reason")

        leave.save()

        messages.success(
            request,
            "Leave Updated Successfully."
        )

        return redirect("leave_list")

    context = {
        "leave": leave,
        "employees": employees,
        "total_employees": employees.count(),
    }

    return render(
        request,
        "edit_leave.html",
        context
    )
