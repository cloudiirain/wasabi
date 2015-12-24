from django.test import TestCase
from django.db import IntegrityError
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
        with self.assertRaises(IntegrityError):
            Series.objects.create(title="OreShura")

class ChapterTestCase(TestCase):
    def setUp(self):
        Series.objects.create(title="OreShura")
        User.objects.create(username="cloudii", email="fake@email.com", password="blah")
        Chapter.objects.create(
            title = "Volume 1 Prologue",
            series = Series.objects.get(title="OreShura"),
            owner = User.objects.get(username="cloudii"),
            order = 0,
            body = "Once upon a time, shuraba happened."
        )
        Chapter.objects.create(
            title = "Volume 1 Chapter 1",
            series = Series.objects.get(title="OreShura"),
            owner = User.objects.get(username="cloudii"),
            order = 1,
            body = "Once upon a time, shuraba happened."
        )

    def test_unicode(self):
        oreshura = Chapter.objects.get(title="Volume 1 Prologue")
        self.assertEqual(oreshura.__unicode__(), "OreShura: Volume 1 Prologue")

    def test_series_and_title_together_is_unique(self):
        with self.assertRaises(IntegrityError):
            Chapter.objects.create(
                title = "Volume 1 Chapter 1",
                series = Series.objects.get(title="OreShura"),
                owner = User.objects.get(username="cloudii"),
                order = 1,
                body = "Once upon a time, shuraba happened."
            )

    def test_insertAt_front(self):
        Chapter.objects.create(
            title = "Volume 1 Illustrations",
            series = Series.objects.get(title="OreShura"),
            owner = User.objects.get(username="cloudii"),
            order = 0,
            body = "Once upon a time, shuraba happened."
        )
        oreshura = Chapter.objects.get(title="Volume 1 Illustrations")
        oreshura.insertAt(oreshura.order)
        self.assertEqual(oreshura.order, 0)
        self.assertEqual(Chapter.objects.get(title="Volume 1 Prologue").order, 1)
        self.assertEqual(Chapter.objects.get(title="Volume 1 Chapter 1").order, 2)

    def test_insertAt_end(self):
        Chapter.objects.create(
            title = "Volume 1 Epilogue",
            series = Series.objects.get(title="OreShura"),
            owner = User.objects.get(username="cloudii"),
            order = 999,
            body = "Once upon a time, shuraba happened."
        )
        oreshura = Chapter.objects.get(title="Volume 1 Epilogue")
        oreshura.insertAt(oreshura.order)
        self.assertEqual(Chapter.objects.get(title="Volume 1 Prologue").order, 0)
        self.assertEqual(Chapter.objects.get(title="Volume 1 Chapter 1").order, 1)
        self.assertEqual(oreshura.order, 2)

    def test_insertAt_middle(self):
        Chapter.objects.create(
            title = "Volume 1 Dedication",
            series = Series.objects.get(title="OreShura"),
            owner = User.objects.get(username="cloudii"),
            order = 1,
            body = "Once upon a time, shuraba happened."
        )
        oreshura = Chapter.objects.get(title="Volume 1 Dedication")
        oreshura.insertAt(oreshura.order)
        self.assertEqual(Chapter.objects.get(title="Volume 1 Prologue").order, 0)
        self.assertEqual(oreshura.order, 1)
        self.assertEqual(Chapter.objects.get(title="Volume 1 Chapter 1").order, 2)

    def test_insertAt_empty(self):
        Series.objects.create(title="OreImo")
        Chapter.objects.create(
            title = "Volume 1 Illustrations",
            series = Series.objects.get(title="OreImo"),
            owner = User.objects.get(username="cloudii"),
            order = 1,
            body = "Once upon a time, there was a siscon."
        )
        oreimo = Chapter.objects.get(title="Volume 1 Illustrations")
        oreimo.insertAt(oreimo.order)
        self.assertEqual(oreimo.order, 0)