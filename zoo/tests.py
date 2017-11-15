from django.test import TestCase

# Create your tests here.
from zoo.models import Animal


class AnimalTestCase(TestCase):

    def setUp(self):
        Animal.objects.create(name="lion", sound="roar")
        Animal.objects.create(name="cat", sound="meow")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Animal.objects.get(name="lion")
        cat = Animal.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')

    def test_str(self):
        """Animals that can speak are correctly identified"""
        lion = Animal.objects.get(name="lion")
        self.assertEqual(lion.__str__(), 'lion')
