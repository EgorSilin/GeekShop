from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'adminapp/index.html')


# READ
def admin_users(request):
    return render(request, 'adminapp/admin-users-read.html')


# CREATE
def admin_users_create(request):
    return render(request, 'adminapp/admin-users-create.html')


# UPDATE and DELETE
def admin_users_update(request):
    return render(request, 'adminapp/admin-users-update-delete.html')


# UPDATE and DELETE
def admin_users_delete(request):
    # return render(request, 'adminapp/admin-users-update-delete.html')
    pass

