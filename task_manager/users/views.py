from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.list import ListView
from task_manager.users.forms import RegisterUserForm, UpdateUserForm
from django.utils.translation import gettext_lazy as _


class UsersIndexView(ListView):
    model = User
    paginate_by = 25
    template_name = 'users/index.html'


class UserFormCreateView(SuccessMessageMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'users/create.html'
    success_url = reverse_lazy("users")
    success_message = _("User was created successfully")


class UserFormUpdateView(SuccessMessageMixin, UpdateView):
    form_class = UpdateUserForm
    template_name = 'users/update.html'
    fields = ['first_name', 'last_name', 'username']
    success_url = reverse_lazy("users")
    success_message = _("User was updated successfully")


class UserFormDeleteView(SuccessMessageMixin, DeleteView):
    model = User
    success_url = reverse_lazy("users")
    success_message = _("User was deleted successfully")