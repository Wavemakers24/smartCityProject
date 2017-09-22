from django.contrib.auth.models import User
from .models import Users
from django import forms
from django.contrib.auth.forms import UserCreationForm

'''class userFrom(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'password2', 'firstname', 'middlename', 'lastname'\
                  , 'gender', 'dob', 'unit', 'street', 'suburb', 'state', 'postcode', 'phoneNumber'\
                  , 'email', 'userType']'''


class registrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Users
        fields = (
            'username',
            'password',
            'password2',
            'firstname',
            'middlename',
            'lastname',
            'email',
            'gender',
            'dob',
             'unit',
            'street',
            'suburb',
            'state',
            'postcode',
            'phoneNumber',
            'userType',
            )

    '''def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.firstname = cleaned_data['firstname']
        user.lastname = cleaned_data['lastname']
        user.email = cleaned_data['email']

        if commit:
            user.save()

        return user'''
