from django.db import models

class Student(models.Model):
    YEAR_CHOICES = [
        ('1st Year', '1st Year'),
        ('2nd Year', '2nd Year'),
        ('3rd Year', '3rd Year'),
        ('4th Year', '4th Year'),
        ('PG - 1st Year', 'PG - 1st Year'),
        ('PG - 2nd Year', 'PG - 2nd Year'),
    ]

    FEE_STATUS_CHOICES = [
        ('Paid', 'Paid'),
        ('Pending', 'Pending'),
        ('Partial', 'Partial'),
    ]

    roll_number = models.CharField(max_length=30, unique=True, verbose_name="Roll Number / Enrollment ID")
    name = models.CharField(max_length=100, verbose_name="Student Name")
    phone = models.CharField(max_length=15, verbose_name="Phone Number")
    email = models.EmailField(max_length=100, verbose_name="Email Address")
    course = models.CharField(max_length=100, verbose_name="Course / Branch")
    academic_year = models.CharField(max_length=50, choices=YEAR_CHOICES, default='1st Year', verbose_name="Academic Year")
    father_name = models.CharField(max_length=100, verbose_name="Father's Name")
    mother_name = models.CharField(max_length=100, verbose_name="Mother's Name")
    abc_id = models.CharField(max_length=50, verbose_name="ABC ID (Academic Bank of Credits)")
    fees = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Total Fees (₹)")
    fees_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Fees Paid (₹)")
    fee_status = models.CharField(max_length=20, choices=FEE_STATUS_CHOICES, default='Pending', verbose_name="Fee Status")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.roll_number}) - {self.course}"

    @property
    def pending_fees(self):
        return max(0, float(self.fees) - float(self.fees_paid))
