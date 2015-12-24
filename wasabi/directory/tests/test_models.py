from django.test import TestCase
from .. models import Series, Chapter
from django.contrib.auth.models import User

class SeriesTestCase(TestCase):
    def setUp(self):
        Series.objects.create(title="OreShura")
        Series.objects.create(title="OreImo")

    def test_unicode(self):
        oreshura = Series.objects.get(title="OreShura")
        self.assertEqual(oreshura.__unicode__(), "OreShura")

    def test_title_is_unique(self):
        pass

class ChapterTestCase(TestCase):
    def setUp(self):
        Series.objects.create(title="OreShura")
        User.objects.create(username="cloudii", email="fake@email.com", password="blah")
        Chapter.objects.create(
            title = "Volume 1 Prologue",
            series = Series.objects.get(title="OreShura"),
            owner = User.objects.get(username="cloudii"),
            order = 1,
            body = "Once upon a time, shuraba happened."
        )

    def test_unicode(self):
        oreshura = Chapter.objects.get(title="Volume 1 Prologue")
        self.assertEqual(oreshura.__unicode__(), "OreShura: Volume 1 Prologue")

    def test_series_and_title_together_is_unique(self):
        pass