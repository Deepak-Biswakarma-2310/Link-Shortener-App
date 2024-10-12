from django.db import models
from django.utils.text import slugify

# create a shortened link - name, url, slug, # of clicks
class Link(models.Model):
    name = models.CharField(max_length=100, unique=True)
    url = models.URLField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    clicks = models.PositiveBigIntegerField(default=0)
    
    # Creating dunder method to show the link names instead of django.object    
    def __str__(self):
        return f"{self.name} | {self.clicks}"
    
    # Creating a method to increment the value of clicks whenever called
    def click(self):
        self.clicks += 1
        self.save()
        
    # Setup the slug field, to autogenerate by overriding the save() method
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            
        return super().save(*args, **kwargs)