from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import RegisterUserForm, ProfileUserForm, UserPasswordChangeForm
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth import logout, get_user_model
from site_grando import settings
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}


def logout_user(request):
    logout(request)
    return redirect('apps.users:login')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    extra_context = {'title': 'Регистрация'}
    success_url = reverse_lazy('apps.users:login')

    def form_invalid(self, form):
        return render(self.request,
                      'users/register_valid_error.html',
                      {'form': form, 'error_message': 'valid error'})


class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'users/profile.html'
    extra_context = {
        'title': 'Профиль пользователя',
        'default_image': settings.DEFAULT_USER_IMAGE
    }

    def get_success_url(self):
        return reverse_lazy('apps.users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("apps.users:password_change_done")
    template_name = "users/password_change_form.html"
