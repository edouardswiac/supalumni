from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from profiles.models import Profile
from supalumni.settings import common
from django.core.exceptions import ObjectDoesNotExist

def _profile_exists(_id_booster):
    try:
        Profile.objects.get(id_booster=_id_booster)
    except ObjectDoesNotExist:
        return False
    return True
    
def _user_exists(_id_booster):
    try:
        User.objects.get(username=_id_booster)
    except ObjectDoesNotExist:
        return False
    return True
    
class RegisterForm(forms.Form):
    id_booster = forms.CharField(min_length=2, max_length=6, required=True, label="Campus ID",
                                 error_messages={'min_length': 'Invalid Campus ID', 'max_length':"Invalid Campus ID"})

    def clean_id_booster(self):
        id = self.cleaned_data['id_booster']
        if not _profile_exists(id) and not _user_exists(id):
            return self.cleaned_data['id_booster']
        else:
            raise forms.ValidationError("Invalid Campus ID")    
    
    def save(self):
        return self.cleaned_data
        
class LoginForm(forms.Form):
    id_booster = forms.CharField(min_length=2, max_length=6, required=True, label="Campus ID",
                                 error_messages={'min_length': 'Invalid Campus ID', 'max_length':"Invalid Campus ID"})    
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    
    def clean(self):
        if self.cleaned_data.get('id_booster') and self.cleaned_data.get('password'):
            if not authenticate(username=self.cleaned_data['id_booster'], password=self.cleaned_data['password']):
                raise forms.ValidationError("Invalid username and/or password")
        
        return self.cleaned_data
    
    def save(self):
        return self.cleaned_data     