from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.list import ListView
from task_manager.users.forms import UserForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import User


class UsersIndexView(ListView):
    model = User
    template_name = 'users/index.html'

    def get_queryset(self):
        return User.objects.filter(is_staff=False)


class UserFormCreateView(SuccessMessageMixin, CreateView):
    form_class = UserForm
    template_name = 'users/create.html'
    success_url = reverse_lazy("users")
    success_message = _("User was created successfully")


class UserFormUpdateView(SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'users/update.html'
    success_url = reverse_lazy("users")
    success_message = _("User was updated successfully")


class UserFormDeleteView(SuccessMessageMixin, DeleteView):
    model = User
    success_url = reverse_lazy("users")
    success_message = _("User was deleted successfully")