from django import forms
from django.forms import ModelForm, Form, IntegerField

from user.models import UserFollowsModel


class UserFollowForm(ModelForm):
    class Meta:
        model = UserFollowsModel
        fields = ['followed_user']


class UnfollowForm(Form):
    followed_user = IntegerField()


class SearchUserForm(forms.Form):
    search = forms.CharField(label="Rechercher un utilisateur")

