from django import forms
from django.contrib.auth.models import User


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    def clean_username(self):
        data = self.cleaned_data.get('username')
        try:
            User.objects.get(username=data)
        except User.DoesNotExist:
            return data
        raise forms.ValidationError('This username is already taken. ')

    def clean_email(self):
        data = self.cleaned_data.get('email')
        try:
            User.objects.get(email=data)
        except User.DoesNotExist:
            return data

        raise forms.ValidationError('This email is already taken. ')

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

