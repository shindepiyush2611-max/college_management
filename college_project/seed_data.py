import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'college_system.settings')
django.setup()

from students.models import Student

sample_students = [
    {
        "roll_number": "CS2024001",
        "name": "Aarav Sharma",
        "phone": "+91 9876543210",
        "email": "aarav.sharma@college.edu",
        "course": "B.Tech - Computer Science",
        "academic_year": "1st Year",
        "father_name": "Rajesh Sharma",
        "mother_name": "Sunita Sharma",
        "abc_id": "ABC-987456321012",
        "fees": 85000.00,
        "fees_paid": 85000.00,
        "fee_status": "Paid",
    },
    {
        "roll_number": "IT2023045",
        "name": "Ananya Patel",
        "phone": "+91 9812345678",
        "email": "ananya.patel@college.edu",
        "course": "B.Tech - Information Technology",
        "academic_year": "2nd Year",
        "father_name": "Vikram Patel",
        "mother_name": "Meena Patel",
        "abc_id": "ABC-654123987456",
        "fees": 90000.00,
        "fees_paid": 45000.00,
        "fee_status": "Partial",
    },
    {
        "roll_number": "BCA2022012",
        "name": "Rohan Gupta",
        "phone": "+91 9765432109",
        "email": "rohan.gupta@college.edu",
        "course": "BCA",
        "academic_year": "3rd Year",
        "father_name": "Suresh Gupta",
        "mother_name": "Pooja Gupta",
        "abc_id": "ABC-321987654321",
        "fees": 60000.00,
        "fees_paid": 0.00,
        "fee_status": "Pending",
    },
    {
        "roll_number": "MCA2024009",
        "name": "Priya Verma",
        "phone": "+91 9988776655",
        "email": "priya.verma@college.edu",
        "course": "MCA",
        "academic_year": "PG - 1st Year",
        "father_name": "Anil Verma",
        "mother_name": "Kavita Verma",
        "abc_id": "ABC-456789123456",
        "fees": 75000.00,
        "fees_paid": 75000.00,
        "fee_status": "Paid",
    },
]

for s_data in sample_students:
    Student.objects.get_or_create(roll_number=s_data["roll_number"], defaults=s_data)

print(f"Successfully seeded {len(sample_students)} students!")
