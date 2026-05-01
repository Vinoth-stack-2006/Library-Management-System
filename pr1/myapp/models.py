from django.db import models

# Create your models here.



class AdminUser(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)  # We'll hash the password for security

    def _str_(self):
        return self.username

class Admin(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)  # (plain text for simplicity)

    def _str_(self):
        return self.username

from django.db import models

class CollegeStudent(models.Model):   # ✅ Student table
    student_id = models.CharField(max_length=100, unique=True)  # Barcode ID
    student_name = models.CharField(max_length=200)             # Student name

    def _str_(self):
        return f"{self.student_name} ({self.student_id})"


class Book(models.Model):   # ✅ Book table
    scanner = models.CharField(max_length=100, unique=True)  # Barcode/Book ID
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, blank=True, null=True)
    year = models.CharField(max_length=10, blank=True, null=True)
    publisher = models.CharField(max_length=50, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    abstract = models.TextField(null=True)
    available = models.BooleanField(default=True) 

    def _str_(self):
        return f"{self.title} ({self.scanner})"

    



from django.db import models
from django.utils import timezone
from django.db import models
from django.db import models
from django.contrib.auth.hashers import make_password

class Student(models.Model):
    student_id = models.CharField(max_length=50, unique=True, null=False, blank=False)
    student_name = models.CharField(max_length=100, null=True, blank=True)  # optional name
    student_email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    last_login = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
  


    def _str_(self):
        return f"{self.student_name or 'Unknown'} ({self.student_id})"



from django.db import models

from django.utils import timezone
from datetime import timedelta

class Borrow(models.Model):
    student_id = models.CharField(max_length=100)
    student_name = models.CharField(max_length=200)
    book_id = models.CharField(max_length=100)
    book_name = models.CharField(max_length=200)
    borrowed_at = models.DateTimeField(auto_now_add=True)
    returned = models.BooleanField(default=False)
    returned_at = models.DateTimeField(null=True, blank=True)
    borrow_duration_days = models.IntegerField(null=True, blank=True)
    
    # ✅ ADD THESE NEW FIELDS
    due_date = models.DateTimeField(null=True, blank=True)  # NEW: 20 days from borrowed_at
    is_overdue = models.BooleanField(default=False)         # NEW: Auto-calculated  
    overdue_days = models.IntegerField(default=0)           # NEW: Days beyond due date
    fine_amount = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)  # NEW: ₹5 per day

    class Meta:
        db_table = "borrow_records"

    def save(self, *args, **kwargs):
    # Auto-set due_date based on user type (if you can determine it)
        if not self.due_date and self.borrowed_at:
            # Default to 20 days for students, but this can be overridden
            self.due_date = self.borrowed_at + timedelta(days=20)
        super().save(*args, **kwargs)

    def calculate_fine(self):
        """Calculate fine for overdue books (₹5 per day after 20 days)"""
        if self.returned:
            return 0  # No fine for returned books
        
        today = timezone.now()
        if self.due_date and today > self.due_date:
            self.overdue_days = (today - self.due_date).days
            self.is_overdue = True
            self.fine_amount = self.overdue_days * 1.00  # ₹1 per day
        else:
            self.overdue_days = 0
            self.is_overdue = False
            self.fine_amount = 0.00
        
        self.save()
        return self.fine_amount

    def _str_(self):
        return f"{self.student_name} - {self.book_name}"


from django.db import models

class BorrowRecord(models.Model):
    student_id = models.CharField(max_length=100)
    student_name = models.CharField(max_length=200)
    book_id = models.CharField(max_length=100)
    book_name = models.CharField(max_length=200)
    borrowed_at = models.DateTimeField(auto_now_add=True)
    returned = models.BooleanField(default=False)
    returned_at = models.DateTimeField(null=True, blank=True)  # ✅ when book is returned
    borrow_duration_days = models.IntegerField(null=True, blank=True)  # ✅ optional: store difference in days

    class Meta:
        db_table = "borrow_record_table"  # 🔹 new table name

    def _str_(self):
        return f"{self.student_name} - {self.book_name}"


from django.db import models

class Gate(models.Model):
    scanner = models.CharField(max_length=100, unique=True)  # Barcode/ID
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, blank=True, null=True)
    year = models.CharField(max_length=10, blank=True, null=True)
    publisher = models.CharField(max_length=50, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    abstract = models.TextField(blank=True, null=True)
    available = models.BooleanField(default=True)

    def _str_(self):
        return f"{self.title} ({self.scanner})"
class IssuedBook(models.Model):   # ✅ new class name
    student_id = models.CharField(max_length=100)
    student_name = models.CharField(max_length=200)
    book_id = models.CharField(max_length=100)
    book_name = models.CharField(max_length=200)
    borrowed_at = models.DateTimeField(auto_now_add=True)
    returned = models.BooleanField(default=False)
    returned_at = models.DateTimeField(null=True, blank=True)
    borrow_duration_days = models.IntegerField(null=True, blank=True)

    def _str_(self):
        return f"{self.student_name} → {self.book_name}"

# Only brands relevant to Tamil Nadu
BRAND_CHOICES = [
    ('DinaThanthi', 'Dina Thanthi'),
    ('Dinamalar', 'Dina Malar'),
    ('TheHindu', 'The Hindu'),
    ('IndianExpress','Indian Express'),
    ('Dinamani','Dina Mani'),
    ]

# Only languages relevant for Tamil Nadu
LANGUAGE_CHOICES = [
    ('TA', 'Tamil'),
    ('EN', 'English'),
]
from django.utils.timezone import now
class Newspaper(models.Model):
    brand = models.CharField(max_length=50, choices=BRAND_CHOICES)
    language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES)

    publish_date = models.DateField(default=now)
    file = models.FileField(upload_to="newspapers/")

    def str(self):
        return f"{self.brand} ({self.language}) - {self.publish_date}"


from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.hashers import make_password

# ===== STAFF MODELS (SEPARATED) =====

class StaffUser(models.Model):
    """Regular Staff Members - Basic Access Only"""
    staff_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    department = models.CharField(max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Hash password before saving
        if not self.password.startswith("pbkdf2_"):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def _str_(self):
        return f"{self.staff_id} - {self.name}"

class HODUser(models.Model):
    """HOD Members - Full Access with Notifications & Purchase Requests"""
    hod_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    department = models.CharField(max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Hash password before saving
        if not self.password.startswith("pbkdf2_"):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def _str_(self):
        return f"{self.hod_id} - {self.name} (HOD)"

# ===== HOD-ONLY NOTIFICATION SYSTEM =====

class HODMessage(models.Model):
    """Notifications for HOD only - replaces StaffMessage"""
    hod = models.ForeignKey(HODUser, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(default=now)
    read = models.BooleanField(default=False)

    def _str_(self):
        return f"Message to {self.hod.name} at {self.created_at}"

# ===== HOD-ONLY PURCHASE REQUEST SYSTEM =====

class PurchaseRequest(models.Model):
    """Purchase requests - HOD only feature"""
    hod_user = models.ForeignKey(HODUser, null=True, blank=True, on_delete=models.SET_NULL)
    hod_name = models.CharField(max_length=100)  # For display
    department = models.CharField(max_length=100)
    book_title = models.CharField(max_length=200)
    author = models.CharField(max_length=150, blank=True, null=True)
    publisher = models.CharField(max_length=150, blank=True, null=True)
    year = models.CharField(max_length=10, blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    request_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected')
    ], default='Pending')
    
    # Audit tracking
    approved_by = models.CharField(max_length=100, blank=True, null=True)
    approved_date = models.DateTimeField(blank=True, null=True)
    
    def _str(self):  # Fixed from _str
        return f"{self.book_title} ({self.hod_name})"

# ===== BACKWARD COMPATIBILITY =====

class Staff(models.Model):
    """Keep existing Staff model for backward compatibility"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    staff_id = models.CharField(max_length=20, unique=True)
    role = models.CharField(max_length=50)
    department = models.CharField(max_length=50)

    def _str_(self):
        return self.user.get_full_name() or self.user.username

# Alias for existing code that references StaffMessage
StaffMessage = HODMessage   

class MainExam(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'main_exam'  # Use existing table name

    def _str_(self):
        return self.name


class SubExam(models.Model):
    main_exam = models.ForeignKey(MainExam, on_delete=models.CASCADE, related_name='subexams')
    name = models.CharField(max_length=200)
    
    class Meta:
        db_table = 'sub_exam'  # Use existing table name

    def _str_(self):
        return f"{self.name} ({self.main_exam.name})"

class Books:
    barcode_image = models.ImageField(upload_to='barcodes/', null=True,blank=True)



    from django.db import models

class Donation(models.Model):
    scanner_id = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    year = models.PositiveIntegerField(null=True, blank=True)
    publisher = models.CharField(max_length=200, null=True, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)
    abstract = models.TextField(null=True, blank=True)
    available = models.CharField(max_length=10, choices=[('Yes','Yes'),('No','No')], default='Yes')

    donor_name = models.CharField(max_length=200, null=True, blank=True)
    donor_type = models.CharField(max_length=100, null=True, blank=True)
    donor_email = models.EmailField(null=True, blank=True)
    donor_phone = models.CharField(max_length=20, null=True, blank=True)
    donor_id = models.CharField(max_length=100, null=True, blank=True)
    donation_date = models.DateField(null=True, blank=True)
    remarks = models.CharField(max_length=300, null=True, blank=True)

    def _str_(self):
        return self.title