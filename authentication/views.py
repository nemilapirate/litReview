from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from django.conf import settings

from . import forms


class LoginView(TemplateView):
    form_class = forms.LoginFrom
    template_name = 'authentication/login.html'

    def get(self, request):
        form = self.form_class
        message = ''
        context = {
            'form': form,
            'message': message
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('flux')

        message = 'Identification invalide'
        context = {
            'form': form,
            'message': message
        }
        return render(request, self.template_name, context)


# Créetion d'un compte
class SignupView(TemplateView):
    form_class = forms.SignupForm
    template_name: str = 'authentication/signup.html'

    def get(self, request):
        form = self.form_class
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT)
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


def logout_user(request):
    logout(request)
    return redirect('login')