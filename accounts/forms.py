from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class RegisterUserForm(UserCreationForm):
    address = forms.CharField(required=True, max_length=120)
    phone = forms.CharField(required=True, max_length=15)
    age = forms.IntegerField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = forms.ChoiceField(choices=GENDER_CHOICES)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'address',
            'phone',
            'age',
            'gender',
            'password1',
            'password2',
        ]