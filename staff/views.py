# staff/views.py
from django.shortcuts import render, redirect
from .models import items
from .forms import ItemRequestForm, ItemStatusUpdateForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

class CustomLoginView(LoginView):
    template_name = 'staff/login.html'
    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated:
            if user.groups.filter(name='Manager').exists():
                return reverse_lazy('staff:manager_dashboard')
            elif user.groups.filter(name='users').exists():
                return reverse_lazy('staff:staff_dashboard')
        return reverse_lazy('staff:login')

def in_manager_group(user):
    return user.groups.filter(name='Manager').exists()

def in_users_group(user):
    return user.groups.filter(name='users').exists()

@login_required
@user_passes_test(in_users_group)
def itemrequest(request):
    if request.method == 'POST':
        form = ItemRequestForm(request.POST)
        if form.is_valid():
            item_request = form.save(commit=False)
            item_request.requested_by = request.user
            item_request.status = 'Pending'
            item_request.save()
            return redirect('staff:success')
    else:
        form = ItemRequestForm()
    return render(request, 'staff/request_item.html', {'form': form})

@login_required
def success_view(request):
    return render(request, 'staff/successpage.html')

@login_required
@user_passes_test(in_users_group)
def staff_dashboard(request):
    queryset = items.objects.filter(requested_by=request.user).order_by('-requested_at')
    return render(request, 'staff/staffdashboard.html', {'items': queryset})  # Changed 'item' to 'items'

@login_required
@user_passes_test(in_manager_group)
def manager_dashboard(request):
    all_requests = items.objects.all().order_by('-requested_at')
    return render(request, 'staff/manager_dashboard.html', {'requests': all_requests})

@login_required
@user_passes_test(in_manager_group)
def update_request_status(request, item_id):
    item = items.objects.get(id=item_id)
    if request.method == "POST":
        status = request.POST.get("status")
        if status in ['Approved', 'Rejected']:
            item.status = status
            item.save()
            return redirect('staff:manager_dashboard')
    return render(request, 'staff/update_request_status.html', {'item': item})

@login_required
@user_passes_test(in_manager_group)
def delete_reviewed_items(request):
    if request.method == "POST":
        items.objects.filter(status__in=['Approved', 'Rejected']).delete()
        return redirect('staff:manager_dashboard')
    return redirect('staff:manager_dashboard')

@login_required
@user_passes_test(in_users_group)
def delete_staff_reviewed_items(request):
    if request.method == "POST":
        items.objects.filter(requested_by=request.user, status__in=['Approved', 'Rejected']).delete()
        return redirect('staff:staff_dashboard')
    return redirect('staff:staff_dashboard')