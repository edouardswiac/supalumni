from django.db import models
from django.template.defaultfilters import slugify
from addresses.models import Address
from profiles.models import Profile

class Company(models.Model):
    class Meta:
        verbose_name_plural = 'companies'
        ordering = ('name', )
    
    name = models.CharField(max_length=100, help_text="Latin alphabet only (including letters like &egrave..")
    name_slug = models.SlugField()
    address = models.ForeignKey(Address)
    website = models.URLField(blank=True)
    
    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        return "/companies/%i/" % self.id
    
    def save(self, force_insert=False, force_update=False):
        self.name_slug = slugify(self.name).lower()
        super(Company, self).save(force_insert, force_update)
        
    
    def first_letter(self):
        return self.name_slug[0]
        
class Position(models.Model):
    class Meta:
        ordering = ('-date_start', )
        
    title = models.CharField(max_length=50, help_text="e.g Java software developer")
    profile = models.ForeignKey(Profile)
    company = models.ForeignKey(Company)
    date_start = models.DateField();
    date_end = models.DateField(null=True);
    
    def __unicode__(self):
        return '%s %s' % (self.title, self.company.name)
    