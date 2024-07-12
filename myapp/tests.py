from django.test import TestCase


class SimpleTest(TestCase):
    def test_addition(self):
        self.assertEqual(1 + 3, 2)
