from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    phone = forms.CharField(max_length=20, required=False, label='Телефон')
    is_subscribed = forms.BooleanField(required=False, label='Подписаться на новости')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'phone', 'password1', 'password2', 'is_subscribed')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'phone', 'avatar', 'is_subscribed')