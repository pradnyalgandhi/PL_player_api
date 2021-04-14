from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class ConsumerForm(UserCreationForm):
    
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)

    class Meta:
        model = User
        fields = ["username","first_name","last_name","email","password1","password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'First Name'
        })
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Last Name'
        })
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Username'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'type' : 'email',
            'placeholder': 'Email ID',
            'data-rule': 'email',
            'data-msg': 'Please enter a valid email'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'type': 'password',
            'placeholder': 'Password',
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'type': 'password',
            'placeholder': 'Confirm Password',
        })

    def clean(self):
        cleaned_data = super(ConsumerForm, self).clean()
        password = cleaned_data.get('password1')
        confirm_password = cleaned_data.get('password2')

        if password == "" or password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
