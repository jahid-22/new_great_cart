from django.contrib.auth.forms import UserChangeForm, UserCreationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm, AuthenticationForm
from django import forms
from . models import Country, Person
# from . models import Person

# User Registration form
class CustomUserForm(forms.ModelForm):
    class Meta:
        model = Person
        
        # fields = "__all__"
        fields = ['first_name', 'last_name','email','phone','gender','city','country','password']
        def __init__(self):
            super().__init__(*args, **kwargs)
            # Customize the country select options dynamically
            self.fields['country'].queryset = Country.objects
        
        widgets = {
            'first_name' :forms.TextInput(attrs={"class":"form-control"}),
            'last_name' :forms.TextInput(attrs={"class":"form-control"}),
            'email' :forms.EmailInput(attrs={"class":"form-control"}),
            'phone' :forms.TextInput(attrs={"class":"form-control"}),
            'gender' :forms.Select(attrs={"class":"form-control"}),
            'city' :forms.TextInput(attrs={"class":"form-control"}),
            'country' :forms.Select(attrs={"class":"form-control"}),
            'password' :forms.PasswordInput(attrs={"class":"form-control"})
        }


        
        