from django.contrib.auth.forms import UserCreationForm, User


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']

    def clean_username(self):
        return self.cleaned_data['username']
