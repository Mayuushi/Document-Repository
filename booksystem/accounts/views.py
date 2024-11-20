from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm, AdminRegisterForm
from django.contrib.auth.decorators import login_required
from .models import CustomUser  # Import your custom user model
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ValidationError
from .forms import UserRegisterForm, AdminRegisterForm

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Add custom validation: Password and email must not be similar
            password = form.cleaned_data.get("password1")  # Assuming you're using a two-password field
            email = form.cleaned_data.get("email")
            if email and password and email.lower() in password.lower():
                messages.error(request, "Password and email must not be similar.")
            else:
                try:
                    form.save()  # Save the user to the database
                    messages.success(request, "Registration successful! You can now log in.")
                    return redirect('login')  # Redirect to the login page after successful registration
                except ValidationError as e:
                    # Log or display the error details for debugging
                    messages.error(request, f"Error saving user: {', '.join(e.messages)}")
        else:
            # Provide feedback on invalid form inputs
            messages.error(request, "Invalid username and password")
            for field, errors in form.errors.items():
                messages.error(request, f"{field.capitalize()}: {', '.join(errors)}")
    else:
        form = UserRegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


def admin_register(request):
    if request.method == 'POST':
        form = AdminRegisterForm(request.POST)
        
        # Check the admin access code
        admin_code = request.POST.get('admin_code')
        if not admin_code:
            messages.error(request, "Admin access code is required.")
            return redirect('admin_register')
        elif admin_code != "123456":
            messages.error(request, "Invalid admin access code.")
            return redirect('admin_register')

        if form.is_valid():
            try:
                form.save()  # Save the admin user
                messages.success(request, "Admin registered successfully!")
                return redirect('login')
            except ValidationError as e:
                # Log or display the error details for debugging
                messages.error(request, f"Error saving admin: {', '.join(e.messages)}")
        else:
            # Provide feedback on invalid form inputs
            messages.error(request, "Invalid username and password")
            for field, errors in form.errors.items():
                messages.error(request, f"{field.capitalize()}: {', '.join(errors)}")
    else:
        form = AdminRegisterForm()

    return render(request, 'accounts/admin_register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Authenticate user based on email instead of username
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            # Check if the user is an admin
            if user.is_superuser:
                return redirect('book_list')  # Redirect admin to book_list
            else:
                return redirect('book_list_user')  # Redirect regular user to home
        else:
            messages.error(request, "Invalid email or password.")
            return redirect('login')  # Redirect to login on failure

    return render(request, "accounts/login.html")