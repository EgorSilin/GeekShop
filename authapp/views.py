from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from authapp.forms import UserLoginForm, UserCreationForm, UserRegisterForm, UserProfileForm
from basketapp.models import Basket


# Create your views here.
class Login(LoginView):
    form_class = UserLoginForm
    template_name = 'authapp/login.html'


class Register(SuccessMessageMixin, CreateView):
    form_class = UserRegisterForm
    template_name = 'authapp/register.html'
    success_url = reverse_lazy('auth:login')
    success_message = "Successfully registered!"


@login_required()
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('auth:profile'))
    else:
        form = UserProfileForm(instance=request.user)
    baskets = Basket.objects.filter(user=request.user)

    context = {
        'form': form,
        'baskets': baskets,
        # 'total_quantity': total_quantity,
        # 'total_sum': total_sum
    }
    return render(request, 'authapp/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))

