# Create your views here.
from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Department, Course
from django.http import JsonResponse


def student_registration(request):
    # Get department_id from POST data if form is submitted, otherwise None
    department_id = request.POST.get('department') if request.method == 'POST' else None
    form = StudentForm(request.POST or None, department_id=department_id)

    if form.is_valid():
        form.save()  # Save the valid form
        return redirect('student_success')  # Use the correct success URL name here

    return render(request, 'registration/student_registration.html', {'form': form})


def load_courses(request):
    # Get department ID from GET data
    department_id = request.GET.get('department_id')
    courses = Course.objects.filter(department_id=department_id).all()
    
    # Return course data as JSON
    return JsonResponse(list(courses.values('id', 'name')), safe=False)


def student_success(request):
    # Render a success page after successful registration
    return render(request, 'registration/success.html')

def home(request):
    return render(request, 'registration/home.html')