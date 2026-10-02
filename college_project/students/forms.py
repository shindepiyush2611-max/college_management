from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'roll_number',
            'name',
            'phone',
            'email',
            'course',
            'academic_year',
            'father_name',
            'mother_name',
            'abc_id',
            'fees',
            'fees_paid',
            'fee_status',
        ]
        widgets = {
            'roll_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. CS2024001'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter full student name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. +91 9876543210'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'student@college.edu'}),
            'course': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. B.Tech Computer Science'}),
            'academic_year': forms.Select(attrs={'class': 'form-select'}),
            'father_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter father's full name"}),
            'mother_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter mother's full name"}),
            'abc_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '12-digit Academic Bank of Credits ID'}),
            'fees': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': '0.00'}),
            'fees_paid': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': '0.00'}),
            'fee_status': forms.Select(attrs={'class': 'form-select'}),
        }
