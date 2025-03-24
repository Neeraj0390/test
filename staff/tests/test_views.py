import pytest
from django.urls import reverse
from django.contrib.auth.models import User, Group
from staff.models import items

# Setup a staff user (reusable code called a fixture)
@pytest.fixture
def staff_user():
    user = User.objects.create_user(username='staff1', password='test123')
    group, _ = Group.objects.get_or_create(name='users')  # Create 'users' group
    user.groups.add(group)  # Add user to group
    return user

# Test the staff dashboard
@pytest.mark.django_db
def test_staff_dashboard(client, staff_user):
    # Log in the staff user
    client.login(username='staff1', password='test123')
    
    # Visit the staff dashboard
    url = reverse('staff:staff_dashboard')  # Gets the URL from your URL names
    response = client.get(url)
    
    # Check if the page loads (status code 200 means success)
    assert response.status_code == 200

# Test item request submission
@pytest.mark.django_db
def test_item_request(client, staff_user):
    client.login(username='staff1', password='test123')
    
    # Data for the new item request
    data = {
        'item_name': 'Chair',
        'quantity': 2,
        'urgency': 'High',
        'category': 'Equipment',
        'department_section': 'Dining',
        'reason': 'Broken'
    }
    
    # Submit the form
    url = reverse('staff:itemrequest')
    response = client.post(url, data)
    
    # Check if it redirects (302 means redirect after success)
    assert response.status_code == 302
    # Check if the item was created
    assert items.objects.filter(item_name='Chair').exists()