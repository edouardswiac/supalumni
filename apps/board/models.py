import datetime
from django.db import models
from django.contrib.auth.models import User
from users.models import Profile

class Category(models.Model):
    name = models.CharField(max_length=30)
    
    class Meta:
        verbose_name_plural = 'categories'
        ordering = ('name', )
        
    def __unicode__(self):
        return self.name
        
class Post(models.Model):
    author = models.ForeignKey(Profile)
    title = models.CharField(max_length=35)
    content = models.TextField()
    category = models.ForeignKey(Category)
    date_posted = models.DateTimeField(editable=False)
    
    class Meta:
        ordering = ('-date_posted', )
        
    def __unicode__(self):
        return self.title
    
    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.date_posted = datetime.datetime.now()
        super(Post, self).save(force_insert, force_update)