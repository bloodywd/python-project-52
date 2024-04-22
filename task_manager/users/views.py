from django.contrib.auth.mixins import LoginRequiredMixin
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

    def get_queryset(self):
        return get_user_model().objects.filter(is_staff=False)


class UserFormCreateView(SuccessMessageMixin, CreateView):
    form_class = UserForm
    template_name = 'users/user_form.html'
    success_url = reverse_lazy("users")
    success_message = _("User was created successfully")
    extra_context = {'title': "Create user", 'button_name': 'Create'}


class UserFormUpdateView(SelfActionPermissionMixin, SuccessMessageMixin, UpdateView):
    model = get_user_model()
    form_class = UserForm
    template_name = 'users/user_form.html'
    success_url = reverse_lazy("users")
    success_message = _("User was updated successfully")
    extra_context = {'title': "Edit user", 'button_name': 'Edit'}
    permission_denied_message = 'You cant edit other users'


class UserFormDeleteView(SelfActionPermissionMixin, SuccessMessageMixin, DeleteView):
    model = get_user_model()
    template_name = 'users/user_delete.html'
    success_url = reverse_lazy("users")
    success_message = _("User was deleted successfully")
    permission_denied_message = 'You cant delete other users'
