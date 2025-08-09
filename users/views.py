from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import StudentRegistrationForm
from .models import Student  # your custom model: users_student

# 🟢 Sign In View
def SignIn(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('/')  # or 'dashboard'
        else:
            messages.error(request, "Invalid login credentials.")
    else:
        form = AuthenticationForm()

        if 'next' in request.GET:
            messages.info(request, "Please sign in to access that page.")


    return render(request, 'user/signIn.html', {'form': form})


# 🟢 Register View
def Register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            student = Student.objects.create(
                user=user,
                full_name=form.cleaned_data['full_name'],
                dob=form.cleaned_data['dob'],
                year=form.cleaned_data['year'],
                prn=form.cleaned_data['prn']
            )
            if 'email' in form.cleaned_data and form.cleaned_data['email']:
                user.email = form.cleaned_data['email']
                user.save()

            login(request, user)
            messages.success(request, f"Registration successful for {user.username}!")
            return redirect('/')
        else:
            # ✅ Clear old error messages before adding new
            storage = messages.get_messages(request)
            storage.used = True  # Clear previous messages

            messages.error(request, "Registration failed. Please correct the errors below.")
    else:
        form = StudentRegistrationForm()

    return render(request, 'user/register.html', {'form': form})



# 🔴 Logout View
def LogoutUser(request):
    logout(request)
    messages.success(request, "You've been logged out successfully!")
    return redirect('/')


# 🟡 Optional: Dashboard View (Login Required)
@login_required(login_url='signIn')
def Dashboard(request):
    return render(request, 'index.html')
