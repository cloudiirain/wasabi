from django.db import models

"""
A novel series
"""
class Series(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['title']


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
        ordering = ['series', 'order']

    """
    Insert chapter at the specified position in the order. This is a 0-based insertion.

    chapter.insertAt(0) - inserts the chapter at the beginning of the series list
    chapter.insertAt(2) - inserts the chapter at the 3rd position in the series list
    chapter.insertAt(999) - for index out of bounds, insert the chapter at the end
    chapter.insertAt(-1) - insert the chapter at the end for any negative number
    """
    def insertAt(self, index):
        series_chapters = self.series.chapters.all().exclude(pk=self.pk)
        i = 0
        if index >= len(series_chapters) or index < 0:
            # Add to the end of the list; re-order the entire list as a safety precaution
            for chapter in series_chapters:
                chapter.order = i
                chapter.save()
                i += 1
            self.order = i
            self.save()
        else:
            # Add the chapter somewhere in the middle or beginning of the list
            for chapter in series_chapters[:index]:
                chapter.order = i
                chapter.save()
                i += 1
            self.order = i
            i += 1
            for chapter in series_chapters[index:]:
                chapter.order = i
                chapter.save()
                i += 1