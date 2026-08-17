from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


# Home Page
def home(request):
    return render(request, 'index.html')

# User Signup Function
def signup(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Check password
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return render(request,'signup.html')

        # check username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return render(request, 'signup.html')

        # Create User
        user = User.objects.create_user(
            username=username,
            password=password
        )

        messages.success(request, "Account created successfully. Please login.")
        return redirect('login')
    return render(request, 'signup.html')

# User Login Function
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,username=username,
            password=password
        )

        if user:
            login(request, user)
            return redirect("employee_list")

        else:
            messages.error(request, "Invalid Username or Password")
            return render(request,'login.html')

# User Logout Function
def user_logout(request):
        logout(request)
        return redirect

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