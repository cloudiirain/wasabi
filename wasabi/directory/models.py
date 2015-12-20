from django.db import models
from django.utils.text import slugify

class Series(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return self.title

class Page(models.Model):
    title = models.CharField(max_length=100)
    series = models.ForeignKey(Series, related_name='pages')
    owner = models.ForeignKey('auth.User', related_name='pages', default=None)
    order = models.IntegerField()
    body = models.TextField()

    def __unicode__(self):
        return str(self.series) + ": " + str(self.title)

    class Meta:
        unique_together = ('series', 'title')
    
