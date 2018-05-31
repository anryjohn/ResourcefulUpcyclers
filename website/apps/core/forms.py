
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
"""
class SignUpForm(UserCreationForm):

    # Sign Up Form fields, add extra info you'd like the user to put in their profile here
    first_name = forms.CharField(max_length=30, required=True, help_text='')
    last_name = forms.CharField(max_length=30, required=True, help_text='')
    email = forms.EmailField(max_length=300, help_text='*Required. Must be valid email address.')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, help_text='Must be at least 8 characters.')
    birth_date = forms.DateField(help_text='Format: YYYY-MM-DD')
    bio = forms.CharField(help_text='Enter tags here.')
    owner_key = forms.CharField(max_length=32, required=False, help_text='If you have a upgrade to a Business Profile, enter your key here.')
    #profile_image = forms.ImageField(help_text='Upload a profile image')

    # Be sure to add extra fields here
    class Meta:
        model = User
        fields = (  'username',
                    'first_name',
                    'last_name',
                    'email',
                    'password1',
                    'password2',
                    'birth_date',
                    'bio',
                    'owner_key'
                    #'profileimage',
                    )
"""
