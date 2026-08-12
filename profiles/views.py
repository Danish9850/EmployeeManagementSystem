from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from employees.models import Employee
from leaves.models import Leave
from tasks.models import Task
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth import update_session_auth_hash

# Create your views here.
@login_required
def profile(request):

    context = {
        "total_employees":
        Employee.objects.count(),
        "total_leaves":Leave.objects.count(),
        "total_tasks":Task.objects.count(),
    }

    return render(request, "profile.html", context)
def edit_profile(request):
    user = request.user
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        user.username = username
        user.email = email
        user.save()

        messages.success(request, "Profile updated successfully!")
        return redirect("profile")
    return render(request, "edit_profile.html")

def change_password(request):

    if request.method == "POST":

        old_password = request.POST.get("old_password")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        if not request.user.check_password(old_password):
            messages.error(request, "Old password is incorrect.")
            return redirect("change_password")

        if new_password != confirm_password:
            messages.error(request, "New passwords do not match.")
            return redirect("change_password")

        request.user.set_password(new_password)
        request.user.save()

        update_session_auth_hash(request, request.user)

        messages.success(request, "Password changed successfully!")

        return redirect("profile")

    return render(request, "change_password.html")
    
