import pytest
from django.contrib.auth.models import User
from staff.models import items  # Your model name


# This tells pytest to use the database
@pytest.mark.django_db
def test_create_item():
    # Create a test user
    user = User.objects.create_user(username='testuser', password='test123')
    
    # Create an item
    item = items.objects.create(
        item_name='Pencil',
        quantity=10,
        status='Pending',
        requested_by=user,
        urgency='Low',
        category='Supplies',
        department_section='General',
        reason='Running Low'
    )
    
    # Check if the item was created correctly
    assert item.item_name == 'Pencil'  # Did the name save?
    assert item.quantity == 10         # Did the quantity save?
    assert item.requested_by.username == 'testuser'  # Is the right user linked?
    assert str(item) == 'Pencil - Pending'  # Does the string representation work?