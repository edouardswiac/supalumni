from django import forms
from django.template.defaultfilters import slugify
from widgets import MonthYearWidget
from .models import Company, Position
import string 
import datetime

position_years = range(datetime.date.today().year, datetime.date.today().year-30, -1)
class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ('address', 'name_slug',)
    
    def clean_name(self):
        valid = string.ascii_lowercase + string.digits
        slugged = slugify(self.cleaned_data['name']).lower()
        if len(slugged) == 0:
            raise forms.ValidationError("Must be composed of latin alphabet")
        
        return self.cleaned_data['name']

class PositionForm(forms.Form):
    company = forms.ModelChoiceField(queryset=Company.objects.all())
    title = forms.CharField(help_text="e.g Java software engineer, Project manager")
    start_date = forms.DateField(widget=MonthYearWidget(years=position_years))
    end_date = forms.DateField(label="End date", help_text="Do not specify an end date if the position is held", widget=MonthYearWidget(years=position_years), required=False)
        
    def save(self):
        position = Position()
        position.company = self.cleaned_data['company']
        position.title = self.cleaned_data['title']
        position.date_start = self.cleaned_data['start_date']
        position.date_end = self.cleaned_data['end_date'] if self.cleaned_data['end_date'] else None
        return position
    