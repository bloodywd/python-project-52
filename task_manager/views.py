from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from .forms import LoginUserForm


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'
    extra_context = {'title': "Login"}

    def get_success_url(self):
        return reverse_lazy('index')
