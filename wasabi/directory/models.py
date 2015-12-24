from django.db import models

"""
A novel series
"""
class Series(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return self.title

"""
A chapter from a novel series
"""
class Chapter(models.Model):
    title = models.CharField(max_length=100)
    series = models.ForeignKey(Series, related_name='chapters')
    owner = models.ForeignKey('auth.User', related_name='chapters', default=None)
    order = models.IntegerField()
    body = models.TextField()

    def __unicode__(self):
        return str(self.series) + ": " + str(self.title)

    class Meta:
        unique_together = ('series', 'title')

    """
    Need to build a reordering function that allows us to insert a chapter into a particular position in the order.
    """
    def insert_chapter(self):
        pass

