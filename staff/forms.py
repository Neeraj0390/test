# staff/forms.py
from django import forms
from .models import items

# Staff Form
class ItemRequestForm(forms.ModelForm):
    class Meta:
        model = items
        fields = ['item_name', 'quantity', 'urgency', 'category', 'department_section', 'reason']
        exclude = ['requested_by', 'status', 'requested_at']
        widgets = {
            'item_name': forms.TextInput(attrs={'placeholder': 'Item Name'}),
            'quantity': forms.NumberInput(attrs={'placeholder': 'Quantity'}),
            'urgency': forms.Select(),
            'category': forms.Select(),
            'department_section': forms.Select(),
            'reason': forms.Select(),
        }

# Manager Form
class ItemStatusUpdateForm(forms.ModelForm):
    class Meta:
        model = items
        fields = ['status']
        widgets = {
            'status': forms.Select(),
        }