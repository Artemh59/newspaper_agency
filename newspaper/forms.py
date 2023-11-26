from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from newspaper.models import Newspaper, Redactor


class NewForm(forms.ModelForm):
    redactor = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Newspaper
        fields = "__all__"


class SignUpForm(UserCreationForm):
    class Meta:
        model = Redactor
        fields = ('username', 'email', 'password1', 'password2')
