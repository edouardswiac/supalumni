from django.db import models
from django_countries.fields import CountryField
import gmaps

class Address(models.Model):
    street1 = models.CharField(max_length=100)
    street2 = models.CharField(max_length=100, blank=True)
    zipcode = models.CharField(max_length=15)
    city = models.CharField(max_length=35)
    country = CountryField()
    lat = models.FloatField()
    long = models.FloatField()
    
    class Meta:
        verbose_name_plural = 'addresses'
        ordering = ('country', 'city')
        
    def __unicode__(self):
        return u"%s %s %s %s %s" % (self.street1, self.street2, self.zipcode, self.city, self.country.name)
    
    # throw exception if unable to geocode
    def save(self, force_insert=False, force_update=False):
        self.city = self.city.capitalize()
        # update geocoding infos
        try:
            loc = gmaps.geocode(self.__unicode__())
        except Exception:
            return False
        
        self.lat = loc['lat']
        self.long = loc['lng']
        super(Address, self).save(force_insert, force_update)
