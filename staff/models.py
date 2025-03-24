# staff/models.py
from django.db import models
from django.contrib.auth.models import User

class items(models.Model):
    item_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending')
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE)
    requested_at = models.DateTimeField(auto_now_add=True)
    
    # New Fields
    urgency = models.CharField(max_length=20, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], default='Medium')
    category = models.CharField(max_length=50, choices=[
        ('Supplies', 'Supplies'), ('Equipment', 'Equipment'), ('Food', 'Food'),  ('Other', 'Other')
    ], default='Supplies')
    department_section = models.CharField(max_length=50, choices=[
        ('Kitchen', 'Kitchen'), 
        ('Bar', 'Bar'), 
        ('Dining', 'Dining'), 
        ('General', 'General')
    ], default='General')
    reason = models.CharField(max_length=50, choices=[
        ('Running Low', 'Running Low'), 
        ('Broken', 'Broken'), 
        ('New Event', 'New Event'), 
        ('Other', 'Other')
    ], default='Running Low')

    def __str__(self):
        return f"{self.item_name} - {self.status}"