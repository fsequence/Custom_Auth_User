import unicodedata
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


# looked at the source code and UserCreationForm and UserChangeForm
# need/use the class UsernameField, so here it is, included it
class UsernameField(forms.CharField):
    def to_python(self, value):
        return unicodedata.normalize('NFKC', super().to_python(value))


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'password1', 'password2')
        
        # deleted 'username' and put 'email' instead, that should be correct, :]
        field_classes = {'email': UsernameField}


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name',)
       
        # deleted 'username' and put 'email' instead, that should be correct, :]
        field_classes = {'email': UsernameField}

