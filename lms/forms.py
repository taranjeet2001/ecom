from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for frm in self.fields.values():
            frm.widget.attrs['class'] = 'form-control'

class OTPForm(forms.Form):
    otp = forms.CharField(label="Enter OTP", max_length=6, widget=forms.TextInput(attrs={'class': 'form-control'}))
