from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from datetime import datetime
  
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
class userupdateform(forms.ModelForm):
    class Meta: 
        model=CustomUser
        fields = ('username','first_name','last_name','email','is_staff','date_joined','role','is_superuser')
    username = forms.CharField(max_length=150)
    first_name = forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)
    email = forms.EmailField(max_length=254)
    is_staff = forms.BooleanField(initial=False, required=False)
    is_superuser=forms.BooleanField(initial=False,required=False)
    #date_joined=forms.DateField(input_formats=['%Y-%m-%d %H:%M:%S'],widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    date_joined=forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    ROLE_CHOICES = [
      ('admin', 'Admin'),
      ('user', 'User'),
      ('guest', 'Guest'),]
    
    role=forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

class RegistrationForm(UserCreationForm):
      class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2','name','family','email','is_staff','role','date_joined') #,'date_joined',,'is_superuser'
          
      username = forms.CharField(max_length=150)
      password1 = forms.CharField(widget=forms.PasswordInput)
      password2 = forms.CharField(widget=forms.PasswordInput)
      name = forms.CharField(max_length=100)
      family=forms.CharField(max_length=100)
      email = forms.EmailField(max_length=254)
      is_staff = forms.BooleanField(initial=False, required=False)
     # is_superuser=forms.BooleanField(initial=False,required=False)
      #date_joined=forms.DateField(input_formats=['%Y-%m-%d %H:%M:%S'],widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
      date_joined=forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    #  ROLE_CHOICES = [
     #   ('admin', 'Admin'),
      #  ('user', 'User'),
      #  ('guest', 'Guest'),] 
      
     # role=forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
      '''tehran_timezone = pytz.timezone('Asia/Tehran')
      tehran_datetime = timezone.now().astimezone(tehran_timezone)
      date_joined=tehran_datetime'''
      

      def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.password1=self.cleaned_data['password1']
        user.password2=self.cleaned_data['password2']
        user.first_name  = self.cleaned_data['name']
        user.last_name  = self.cleaned_data['family']
        user.email  = self.cleaned_data['email']
        user.is_staff  = self.cleaned_data['is_staff']
        user.date_joined  = datetime.now()#self.cleaned_data['date_joined']
        user.role=self.cleaned_data['role']
      #  user.is_superuser=self.cleaned_data['is_superuser']
        
        if commit:
            user.save()
        return user