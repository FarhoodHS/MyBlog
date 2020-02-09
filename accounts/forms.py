from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class SignupForm(UserCreationForm):
    # email = forms.EmailField(error_messages='Hello')

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'profile_pic',
                  'username', 'password1', 'password2']


# class SignupForm(forms.Form):
#     first_name = forms.CharField(max_length=40, widget=forms.TextInput)
#     last_name = forms.CharField(max_length=40, widget=forms.TextInput)
#     username = forms.CharField(
#         max_length=20, widget=forms.TextInput, required=True)
#     email = forms.EmailField(widget=forms.TextInput, required=True)
#     password = forms.CharField(widget=forms.PasswordInput, required=True)
#     password_confirm = forms.CharField(
#         widget=forms.PasswordInput, required=True)
