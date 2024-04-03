from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class LoginUser(LoginView, SuccessMessageMixin):
    form_class = AuthenticationForm
    template_name = 'login.html'
    extra_context = {'title': "Login"}
    next_page = reverse_lazy('index')
    success_message = _('You are logged in')


def logout_view(request):
    logout(request)
    return redirect('index')
