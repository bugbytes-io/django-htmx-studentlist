from django import forms
from core.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'subject', 'date_of_birth')