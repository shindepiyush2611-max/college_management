from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient
from .forms import PatientForm

# Read: List all patients
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'hospital/patient_list.html', {'patients': patients})

# Create: Add a new patient
def patient_create(request):
    form = PatientForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('patient_list')
    return render(request, 'hospital/patient_form.html', {'form': form})

# Update: Edit patient details
def patient_update(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    form = PatientForm(request.POST or None, instance=patient)
    if form.is_valid():
        form.save()
        return redirect('patient_list')
    return render(request, 'hospital/patient_form.html', {'form': form})

# Delete: Remove a patient
def patient_delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('patient_list')
    return render(request, 'hospital/patient_confirm_delete.html', {'patient': patient})
