from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from task_manager.users.forms import UserForm


# Create your views here.
class UsersIndexView(View):
    def get(self, request, *args, **kwargs):
        users = User.objects.filter(is_staff=False).order_by('id')
        return render(request, 'users/index.html', {"users": users})


class UserFormCreateView(View):
    def get(self, request, *args, **kwargs):
        form = UserForm()
        return render(request, 'users/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserForm()
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Пользователь успешно создан")
            return redirect('users')
        messages.add_message(request, messages.ERROR, "Исправьте ошибки")
        return render(request, 'users/create.html', {'form': form})


class UserFormUpdateView(View):
    pass


class UserFormDeleteView(View):
    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = User.objects.filter(id=user_id).first()
        if user:
            user.delete()
            messages.add_message(request, messages.SUCCESS, "Пользователь успешно удалён")
        return redirect('users')
