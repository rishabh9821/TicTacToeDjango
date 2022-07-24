from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreationForm(UserCreationForm):

    class Meta():
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'userNameInput'
        self.fields['email'].widget.attrs['class'] = 'email'
        self.fields['password1'].widget.attrs['class'] = 'password1'
        self.fields['password2'].widget.attrs['class'] = 'password2'

