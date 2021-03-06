from django.test import TestCase
from .models import Pics, Category, Location
import datetime as dt
from django.urls import reverse

# Create your tests here.


class CategoryTestClass(TestCase):
 # Set up method
    def setUp(self):
        self.type = Category(name='travel')

    def test_instance(self):
        self.assertTrue(isinstance(self.type, Category))

    def test_init(self):

        self.assertTrue(self.type.name == 'travel')

    def test_save_method(self):
        self.type.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_method(self):
        self.type.save_category()
        categories = Category.objects.all()
        self.type.delete_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) == 0)


class LocationTestClass(TestCase):
    def setUp(self):
        self.place = Location(name='lagos')

    def test_instance(self):
        self.assertTrue(isinstance(self.place, Location))

    def test_init(self):
        self.assertTrue(self.place.name == 'lagos')

    def test_save_method(self):
        self.place.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def tearDown(self):
        Location.objects.all().delete()

    def test_delete_method(self):
        self.place.save_location()
        locations = Location.objects.all()
        self.place.delete_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) == 0)


class ImageTestCase(TestCase):
    def setUp(self):
        """
        This will create a new image before each test case
        """
        fun = Category(name="funny")
        fun.save()
        lagos = Location(name="Lagos")
        lagos.save()
        self.new_image = Pics(
            name="image", description="h", location=lagos, category=fun)

    def tearDown(self):
        """
        This will clear the db after each test
        """
        Pics.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()

    def test_instance(self):

        self.assertTrue(isinstance(self.new_image, Pics))

    def test_save_image(self):

        self.new_image.save_image()
        self.assertTrue(len(Pics.objects.all()) > 0)

    def test_filter_by_location(self):

        self.new_image.save_image()
        self.assertTrue(len(Pics.filter_by_location("Lagos")) > 0)

    def test_delete_method(self):
        self.new_image.save_image()
        images = Pics.objects.all()
        self.new_image.delete_image()
        images = Pics.objects.all()
        self.assertTrue(len(images) == 0)

    def test_search_by_category(self):

        self.new_image.save_image()
        self.assertTrue(len(Pics.search_by_category("funny")) > 0)
