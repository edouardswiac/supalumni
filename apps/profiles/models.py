from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.shortcuts import get_object_or_404

def get_promo_years(reverse = True):
    from datetime import datetime
    t = datetime.now()
    start = 1965
    end = t.year + 5
    ranged = range(start, end)
    ranged = ['---'] + ranged
    ranged.sort(reverse = reverse)
    
    return tuple(zip(ranged, ranged))

class Profile(models.Model):
    user = models.OneToOneField(User, unique=True)
    id_booster = models.CharField(max_length=7, primary_key=True)
    last_name_slug = models.SlugField()
    promotion = models.CharField(max_length=4, choices = get_promo_years(), help_text="The year you'll graduate")
    
    description = models.TextField(blank=True, verbose_name="About yourself", help_text="Tell us your plans, your interests")
    website_url = models.URLField(blank=True, verbose_name="Personal website URL", verify_exists=False)
    twitter_url = models.URLField(blank=True, verbose_name="Twitter URL", verify_exists=False)
    facebook_url = models.URLField(blank=True, verbose_name="Facebook URL", verify_exists=False)
    linkedin_url = models.URLField(blank=True, verbose_name="LinkedIn URL", verify_exists=False)
    viadeo_url = models.URLField(blank=True, verbose_name="Viadeo URL", verify_exists=False)
    
    bookmarks = models.ManyToManyField('self', through='Bookmark', symmetrical=False, related_name='related_to')
    
    def add_bookmark_on_profile(self, id_booster):
        profile = get_object_or_404(Profile, id_booster=id_booster)
        b = Bookmark.objects.get_or_create(from_profile=self, to_profile=profile)
        return b

    def remove_bookmark_on_profile(self, id_booster):
        profile = get_object_or_404(Profile, id_booster=id_booster)
        Bookmark.objects.filter(from_profile=self, to_profile=id_booster).delete()
        return
    
    def get_bookmarked_profiles(self):
        return Bookmark.objects.filter(from_profile=self).order_by('to_profile__user__last_name')
    
    def get_who_bookmarked_me(self):
        return Bookmark.objects.filter(to_profile=self).order_by('from_profile__user__last_name')
    
    def set_last_name(self, last_name):
        self.last_name_slug = slugify(last_name)
    
    def delete(self, *args, **kwargs):
        # delete relations
        # User
        User.objects.get(id=self)
        # positions
        Position.objects.filter(profile=self.id_booster).delete()
        # bookmarks
        Bookmarks.objects.filter(from_profile=self.id_booster).delete()
        super(Profile, self).delete(*args, **kwargs)
        
    class Meta:
        ordering = ['id_booster']
      
    def __unicode__(self):
        return '%s %s' % (self.id_booster, self.last_name_slug)
    
    def first_letter(self):
        return self.last_name_slug[0]
    
class Bookmark(models.Model):
    from_profile = models.ForeignKey(Profile, related_name="from_profile")
    to_profile = models.ForeignKey(Profile, related_name="to_profile") 
