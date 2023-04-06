from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


class NewUserForm(UserCreationForm):
    first_name = forms.CharField(required=True, max_length=100)
    last_name = forms.CharField(required=True, max_length=100)
    email = forms.EmailField(required=True, max_length=100, label="Elektro'n Po'chta", initial='admin@gmail.com')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

        def save(self, commit=True):
            user = super(NewUserForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            if commit:
                user.save()
            return user


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('image', 'address', 'bio', 'website')
