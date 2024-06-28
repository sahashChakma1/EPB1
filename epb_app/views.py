from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Report

def home(request):
    if request.method == 'POST':
        course_category = request.POST.get('course_category')
        report_name = request.POST.get('report_name')
        upload_files = request.FILES.get('upload_files')

        if course_category and report_name and upload_files:
            Report.objects.create(
                course_category=course_category,
                report_name=report_name,
                upload_files=upload_files,
            )

            return redirect('success')
            return render(request, 'home.html', {'success': True})  # Indicate success in context

    return render(request, 'home.html')  # Handle GET request

def apply_now(request):
    return render(request, 'apply_now.html')

def success(request):
    return render(request, 'success.html')

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid credentials or not authorized')
        else:
            messages.error(request, 'Invalid credentials or not authorized')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
