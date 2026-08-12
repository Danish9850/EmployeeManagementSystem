from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Home Page
def home(request):
    return render(request, 'index.html')


# User Login Function
def user_login(request):

    # Check if form submitted
    if request.method == 'POST':

        # Get username and password from form
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate user
        user = authenticate(
            request,
            username=username,
            password=password
        )

        # If credentials are correct
        if user:
            login(request, user)            
            return redirect('employee_list')
        else:
            messages.error(request, "Invalid Username or Password")

    
    return render(request, 'login.html')


# User Logout Function
def user_logout(request):
    logout(request)
    return redirect('login')