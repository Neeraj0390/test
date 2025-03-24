import pytest
from django.urls import reverse, resolve

def test_staff_dashboard_url():
    url = reverse('staff:staff_dashboard')  # Get the URL from the name
    assert url == '/staff_dashboard/'  # Check if it matches the expected path
    # 'resolve' checks if the URL points to the right view
    assert resolve(url).func.__name__ == 'staff_dashboard'

def test_item_request_url():
    url = reverse('staff:itemrequest')
    assert url == '/itemrequest/'  # Adjust this based on your actual URL pattern
    assert resolve(url).func.__name__ == 'itemrequest'