"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from populate import movieData


class MovieTest(TestCase):
    def movieBasic(self)
        """
        Tests that movie model can be populated.
        """
        self.assertEqual(1 + 1, 2)
