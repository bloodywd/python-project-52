from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy


class SelfActionPermissionMixin(PermissionRequiredMixin):
    def has_permission(self):
        return self.request.user.pk == self.kwargs['pk']

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            messages.error(self.request, "You need to be logged in")
            return redirect(self.get_login_url())
        else:
            messages.error(self.request, self.permission_denied_message)
            return redirect(reverse_lazy("users"))
