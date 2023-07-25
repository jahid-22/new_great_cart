from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm, AuthenticationForm
from django import forms
# from . models import Person

# User Registration form
class UserRegiForm(UserCreationForm):
    
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )
    
    class Meta:
        model  = Person
        fields = ['first_name','last_name','email','male','female','countty','city']
        widgets = {
            
        }
        
        


