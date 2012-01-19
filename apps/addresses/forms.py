from addresses.models import Address
from django import forms
from . import gmaps

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        # other properties here
        exclude = ('lat', 'long',)
    
    address = None
    def clean(self):
        if self.is_valid():
            address = Address()
            address.street1 = self.cleaned_data['street1']
            address.street2 = self.cleaned_data['street2']
            address.zipcode = self.cleaned_data['zipcode']
            address.city = self.cleaned_data['city']
            address.country = self.cleaned_data['country']
            
            # raise forms exception if not found
            self.set_gmaps_coords(address)
            
            self.address = address
            return self.cleaned_data
    
    def save(self):
        return self.address
    
    # add coords in addre object
    def set_gmaps_coords(self, address):
        loc = None
        try:
            loc = gmaps.geocode(address.__unicode__())
        except Exception:
            raise forms.ValidationError("The address :"+ address.__unicode__() +" can't be found on Google Maps") 
        
        address.lat = loc['lat']
        address.long = loc['lng']
        return