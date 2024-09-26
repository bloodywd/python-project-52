from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.list import ListView
from task_manager.users.forms import UserForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from task_manager.users.utils import SelfActionPermissionMixin


class UsersIndexView(ListView):
    model = get_user_model()
    template_name = 'users/index.html'
    extra_context = {'title': "Users"}


class UserFormCreateView(SuccessMessageMixin, CreateView):
    form_class = UserForm
    template_name = 'form.html'
    success_url = reverse_lazy("login")
    success_message = _("User was created successfully")
    extra_context = {'title': "Create user", 'button_name': 'Create'}


class UserFormUpdateView(SelfActionPermissionMixin, SuccessMessageMixin, UpdateView):
    model = get_user_model()
    form_class = UserForm
    template_name = 'form.html'
    success_url = reverse_lazy("users")
    success_message = _("User was updated successfully")
    extra_context = {'title': "Edit user", 'button_name': 'Save'}
    permission_denied_message = 'You cant edit other users'


class UserFormDeleteView(SelfActionPermissionMixin, SuccessMessageMixin, DeleteView):
    model = get_user_model()
    template_name = 'users/user_delete.html'
    success_url = reverse_lazy("users")
    success_message = _("User was deleted successfully")
    extra_context = {'title': "Delete status"}
    permission_denied_message = 'You cant delete other users'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.has_tasks():
            messages.error(self.request, 'Cant delete active user')
            return redirect(reverse_lazy("users"))
        else:
            self.object.delete()
            return HttpResponseRedirect(self.success_url)
