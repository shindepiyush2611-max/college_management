from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'roll_number',
        'name',
        'course',
        'academic_year',
        'phone',
        'email',
        'abc_id',
        'fees',
        'fee_status',
        'created_at'
    )
    search_fields = ('name', 'roll_number', 'email', 'phone', 'abc_id', 'course')
    list_filter = ('course', 'academic_year', 'fee_status')
    list_per_page = 20
