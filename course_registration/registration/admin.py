from django.contrib import admin

# Register your models here.
from .models import Department, Course, Student

# Register the Department model
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name'] 

# Register the Course model
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'department']     


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'department', 'get_courses']  # Display name, department, and courses

    def get_courses(self, obj):
        # This function will return a comma-separated string of course names
        return ", ".join([course.name for course in obj.courses.all()])

    get_courses.short_description = 'Courses'  # Set the column name in the admin     