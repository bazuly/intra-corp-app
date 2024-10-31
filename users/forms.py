from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django import forms
from .validators import corp_email_validator


class LoginUserForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'password'
        ]
        labels = {
            'username': 'Имя пользователя',
            'password': 'Пароль'
        }


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль, больше 8-ти символов*',
                                widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля',
                                widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-input'}),
                             validators=[corp_email_validator])

    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2'
        ]
        labels = {
            'email': 'E-mail',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }

        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-input'}),
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'})
        }

    def unique_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('Почтовый адрес уже используется')
        return email


class ProfileUserForm(forms.ModelForm):
    username = forms.CharField(disabled=True,
                               label='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.CharField(disabled=True,
                            label='E-mail',
                            widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'email',
            'first_name',
            'last_name'
        ]
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия'
        }


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Старый пароль',
                                   widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password1 = forms.CharField(label='Новый пароль',
                                    widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password2 = forms.CharField(label='Повторите пароль',
                                    widget=forms.PasswordInput(attrs={'class': 'form-input'}))
