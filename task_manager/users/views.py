from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.list import ListView
from task_manager.users.forms import RegisterUserForm


class UsersIndexView(ListView):
    model = User
    paginate_by = 25
    template_name = 'users/index.html'


class UserFormCreateView(SuccessMessageMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'users/create.html'
    success_url = reverse_lazy("users")
    success_message = "User was created successfully"


class UserFormUpdateView(SuccessMessageMixin, UpdateView):
    model = User
    template_name = 'users/update.html'
    fields = ['first_name', 'last_name', 'username']
    success_url = reverse_lazy("users")
    success_message = "User was created updated"


class UserFormDeleteView(SuccessMessageMixin, DeleteView):
    model = User
    success_url = reverse_lazy("users")
    success_message = "User was deleted successfully"
