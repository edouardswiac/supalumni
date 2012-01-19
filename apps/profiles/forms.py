from django import forms
from .models import Profile
from profiles.models import get_promo_years
from tinymce.widgets import TinyMCE
from django.contrib.auth.models import User

class ProfileCoreForm(forms.Form):
    password = forms.CharField(max_length=50, widget=forms.PasswordInput())
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    promotion = forms.TypedChoiceField(choices=get_promo_years(), coerce=int)
    
class ProfileOptionalForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('description', 'website_url', 'twitter_url', 'facebook_url', 'linkedin_url', 'viadeo_url',)
        widgets = {
            'description': TinyMCE(attrs={'cols': 50, 'rows': 10}),
        }
