from django import forms
from .models import Student, Department, Course

class StudentForm(forms.ModelForm):
    department = forms.ModelChoiceField(queryset=Department.objects.all(), required=True, empty_label="Select Department")
    courses = forms.ModelMultipleChoiceField(
        queryset=Course.objects.none(),  # Initially no courses, set dynamically
        widget=forms.CheckboxSelectMultiple,
        required=False
       
    )

    class Meta:
        model = Student
        fields = ['name', 'department', 'courses']

    def __init__(self, *args, **kwargs):
        # Get department_id if passed as a keyword argument
        department_id = kwargs.pop('department_id', None)
        super().__init__(*args, **kwargs)

        if department_id:
            # If department_id is passed, filter courses based on that department
            self.fields['courses'].queryset = Course.objects.filter(department_id=department_id)
        elif self.instance.pk and self.instance.department:
            # If editing an instance, filter courses based on the student's department
            self.fields['courses'].queryset = Course.objects.filter(department=self.instance.department)
        else:
            # If no department is selected, no courses are available
            self.fields['courses'].queryset = Course.objects.none()
