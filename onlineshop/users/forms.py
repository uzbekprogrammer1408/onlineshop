from dataclasses import field
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import CustomUser

class Register(UserCreationForm):
    title = forms.ChoiceField(choices=(
        ('-', '-'),
        ('Mr', 'Mr'),
        ('Mrs', 'Mrs'),
        ('Miss', 'Miss'),        
    ))  
    # date_of_birth = forms.DateField()
    
    email = forms.EmailField(widget = forms.EmailInput(attrs={"placeholder":"email"}))
    first_name = forms.CharField(widget = forms.TextInput(attrs={"placeholder":"first name"}))
    card_number = forms.IntegerField(widget = forms.TextInput(attrs={"placeholder":"card number"}))

    # date_of_birth = forms.DateField(
    #     input_formats=['%d/%m/%Y'],
    #     widget=forms.DateTimeInput(attrs={
    #         'class': 'form-control datetimepicker-input',
    #         'data-target': '#datetimepicker1'
    #     })
    # )
    last_name = forms.CharField(widget = forms.TextInput(attrs={"placeholder":"last name"}))
    password1 = forms.CharField(widget = forms.PasswordInput(attrs={"placeholder":"password"}))
    password2 = forms.CharField(widget = forms.PasswordInput(attrs={"placeholder":"confirm password"}))

    class Meta:
        model = CustomUser
        fields = ('title', 'first_name', 'last_name', 'email', 'password1', 'password2','card_number')

class Login(AuthenticationForm):
    email = forms.EmailField(widget = forms.EmailInput(attrs={"placeholder":"email"}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={"placeholder":"password"}))

    class Meta():
        model = CustomUser
        fields = ('email', 'password')

class LoginForm(forms.Form):
    email = forms.EmailField(widget = forms.EmailInput(attrs={"placeholder":"email"}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={"placeholder":"password"}))