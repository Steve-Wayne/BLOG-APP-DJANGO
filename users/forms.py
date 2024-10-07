# here we create a new form for users to register in order to get extra feilds this form will inherit the default django user form and we will add feilds in this form
from django import forms
from .models import Profile,Contacts
from blog.models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AuthorSearchForm(forms.Form):
    authors = forms.ModelChoiceField(
        queryset=User.objects.all(),  # Queryset of available authors
        widget=forms.Select(attrs={'class': 'form-control'}),  # Optional: Customize the widget
        required=True,  # Make this field required
        label='Select Author'  # Optional: Change the label if needed
    )


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    # warning meta should always writen as Meta as it designs the core structure of the form
    class Meta:
        model = User
        fields = [ 'username', 'email','password1', 'password2']


class UserUpdateform(forms.ModelForm):
    email = forms.EmailField()
    # warning meta should always writen as Meta as it designs the core structure of the form
    class Meta:
        model = User
        fields = [ 'username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image']


class ContactUsForm(forms.ModelForm):
    class Meta:
        model=Contacts
        fields=['name','email' , 'message']