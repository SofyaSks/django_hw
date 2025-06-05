from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput
    )

    password2 = forms.CharField(
        label='Повторите пароль',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = {
            'username': 'Логин',
            'first_name': 'Имя',
            'email': 'Электронная почта'
        }

        help_texts = {
            "username": "Обязательное поле. Буквы, цифры, символ подчеркивания."
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']
    
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)

    class Meta:
        labels = {
            'username': 'Логин',
            'password': 'Пароль'
        }



