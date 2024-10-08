from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'
    extra_context = {'title': _("Main page")}


class LoginUser(SuccessMessageMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'form.html'
    extra_context = {'title': _("Login"), 'button_name': _('Log in')}
    success_message = _('You are logged in')


class LogoutUser(LogoutView):
    def post(self, request, *args, **kwargs):
        messages.success(self.request, _("You are logged out"))
        return super().post(request, *args, **kwargs)
