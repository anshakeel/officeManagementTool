from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,officeId
class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [ 'email',]

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['img' ,'address' , 'phone_no' , 'bio' , 'dob' , 'join_date' , 'exp' , 'age' ]



class addID(forms.ModelForm):
    class Meta:
      model = officeId
      fields = [
        'identification',
          'username',
    ]