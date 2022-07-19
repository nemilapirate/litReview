from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class LoginFrom(forms.Form):
    username = forms.CharField(max_length=50, label="",
                               widget=forms.TextInput(attrs={'placeholder': "Nom d'utilisateur"}))
    password = forms.CharField(max_length=50, label="",
                               widget=forms.PasswordInput(attrs={'placeholder': "Mot de passe"}))


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username',)
