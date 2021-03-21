from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from authapp.models import User
from adminapp.forms import UserAdminRegistrationForm, UserAdminProfileForm


# Create your views here.
@user_passes_test(lambda u: u.is_superuser, login_url='/')
def index(request):
    return render(request, 'adminapp/index.html')


# READ
# @user_passes_test(lambda u: u.is_superuser)
# def admin_users(request):
#     context = {'users': User.objects.all()}
#     return render(request, 'adminapp/admin-users-read.html', context)
class UserListView(ListView):
    model = User
    template_name = 'adminapp/admin-users-read.html'
    # queryset = User.objects.filter(is_active=True)


# CREATE
# @user_passes_test(lambda u: u.is_superuser)
# def admin_users_create(request):
#     if request.method == 'POST':
#         form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admin_staff:admin_users'))
#     else:
#         form = UserAdminRegistrationForm()
#     context = {'form': form}
#     return render(request, 'adminapp/admin-users-create.html', context)
class UserCreateView(CreateView):
    model = User
    template_name = 'adminapp/admin-users-create.html'
    form_class = UserAdminRegistrationForm
    success_url = reverse_lazy('admin_staff:admin_users')


# UPDATE
@user_passes_test(lambda u: u.is_superuser)
def admin_users_update(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = UserAdminProfileForm(data=request.POST, files=request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_users'))
    else:
        form = UserAdminProfileForm(instance=user)
    context = {
        'form': form,
        'user': user,
    }
    return render(request, 'adminapp/admin-users-update-delete.html', context)


# DELETE
@user_passes_test(lambda u: u.is_superuser)
def admin_users_delete(request, user_id):
    user = User.objects.get(id=user_id)
    # user.delete()
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('admin_staff:admin_users'))

