from django import forms
from .models import UserInfo, UserPost
from django.contrib.auth.models import User

class UserInfoForm(forms.ModelForm):
    class Meta():
        model = UserInfo
        fields = ('portfolio', 'profile_pic')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserPostForm(forms.ModelForm):
    class Meta():
        model = UserPost
        fields = '__all__'