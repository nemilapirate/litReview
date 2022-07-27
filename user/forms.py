from django import  forms
from django.forms import ModelForm, Form, IntegerField

from user.models import Userfollows


class UserfollowForm(ModelForm):
    class Meta:
        model = Userfollows
        fields = "'followed_user"
        labels = "followed_user"


class UnfollowForm(Form):
    followed_user = IntegerField()


class SearchUser(forms.Form):
    search = forms.CharField(label="Rechercher un utilisateur")

