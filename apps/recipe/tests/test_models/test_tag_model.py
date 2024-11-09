from django.test import TestCase
from django.contrib.auth import get_user_model

from apps.recipe import models


def sample_user(email='test@gmail.com', password='test123'):
    return get_user_model().objects.create_user(email=email, password=password)


class TagModelTests(TestCase):
    def test_create_tag(self):
        """Test tag string representation."""
        tag = models.Tag.objects.create(name='Vegan', user=sample_user())

        self.assertEqual(str(tag), tag.name)
