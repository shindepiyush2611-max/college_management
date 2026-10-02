from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q, Sum
from .models import Student
from .forms import StudentForm

# Read: List all students with search, filter, and analytics summary
def student_list(request):
    query = request.GET.get('q', '').strip()
    course_filter = request.GET.get('course', '').strip()
    year_filter = request.GET.get('year', '').strip()

    students = Student.objects.all()

    if query:
        students = students.filter(
            Q(name__icontains=query) |
            Q(roll_number__icontains=query) |
            Q(email__icontains=query) |
            Q(phone__icontains=query) |
            Q(course__icontains=query) |
            Q(abc_id__icontains=query) |
            Q(father_name__icontains=query) |
            Q(mother_name__icontains=query)
        )

    if course_filter:
        students = students.filter(course=course_filter)

    if year_filter:
        students = students.filter(academic_year=year_filter)

    # Analytics metrics
    all_students = Student.objects.all()
    total_students = all_students.count()
    total_fees = all_students.aggregate(Sum('fees'))['fees__sum'] or 0
    total_fees_paid = all_students.aggregate(Sum('fees_paid'))['fees_paid__sum'] or 0
    total_pending_fees = max(0, total_fees - total_fees_paid)
    
    distinct_courses = Student.objects.values_list('course', flat=True).distinct()
    distinct_years = Student.YEAR_CHOICES

    context = {
        'students': students,
        'query': query,
        'course_filter': course_filter,
        'year_filter': year_filter,
        'total_students': total_students,
        'total_fees': total_fees,
        'total_fees_paid': total_fees_paid,
        'total_pending_fees': total_pending_fees,
        'distinct_courses': distinct_courses,
        'distinct_years': distinct_years,
    }
    return render(request, 'students/student_list.html', context)


# Read: View individual student detail
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/student_detail.html', {'student': student})


# Create: Add a new student
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            messages.success(request, f"Student '{student.name}' added successfully!")
            return redirect('student_list')
        else:
            messages.error(request, "Please correct the errors in the form.")
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form, 'title': 'Add New Student'})


# Update: Edit student details
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, f"Student '{student.name}' updated successfully!")
            return redirect('student_list')
        else:
            messages.error(request, "Please correct the errors in the form.")
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_form.html', {'form': form, 'student': student, 'title': f'Edit Student: {student.name}'})


# Delete: Remove a student
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student_name = student.name
        student.delete()
        messages.success(request, f"Student '{student_name}' deleted successfully!")
        return redirect('student_list')
    return render(request, 'students/student_confirm_delete.html', {'student': student})
