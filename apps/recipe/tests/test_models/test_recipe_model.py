from django.contrib.auth import get_user_model
from django.test import TestCase
from unittest.mock import patch
from apps.recipe import models


def sample_user(email='test@gmail.com', password='test123'):
    return get_user_model().objects.create_user(email=email, password=password)


class RecipeModelTests(TestCase):
    def test_recipe_str(self):
        """Test the string representation of a Recipe model."""
        recipe = models.Recipe.objects.create(
            user=sample_user(),
            title='Test Recipe',
            time_minutes=10,
            price=10.00
        )

        self.assertEqual(str(recipe), 'Test Recipe')

    @patch('uuid.uuid4')
    def test_recipe_file_name_uuid(self, mock_uuid):
        """Test that image is saved in the correct location"""
        uuid = 'test-uuid'
        mock_uuid.return_value = uuid
        file_path = models.recipe_image_file_path(None, 'myimage.jpg')

        exp_path = f'uploads/recipe/{uuid}.jpg'
        self.assertEqual(file_path, exp_path)
