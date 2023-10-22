from django.contrib.auth.forms import UserCreationForm

from .models import User
from django import forms


'''This is used to create a form for registering users and this is inbuilt django forms which is more secured and 
to create a form we are importing usercreationform which is available inbuilt in django'''

class CustomUserCreation(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Enter Username'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Enter Emailid'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2','placeholder':'Enter Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2','placeholder':'Confirm Password'}))
    '''These foyr username ,email,password1 and password2 are the necessary details we are going to save from the user'''

    class Meta:
        model = User #This User is also available inbuilt in out database as auth_user
        fields = ['username','email','password1','password2']