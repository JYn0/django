from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
# 회원가입 form, 로그인(인증) form
from .models import User

class CustomUserCreationForm(UserCreationForm):
    address = forms.CharField(min_length=3)
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('address', ) # 원래 있던 field에 address도 추가

class CustomAuthenticationForm(AuthenticationForm):
    class Meta(AuthenticationForm):
        model = User