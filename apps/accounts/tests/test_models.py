from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful."""
        email = 'mdn1376@gmail.com'
        password = 'pass123'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized."""
        email = 'test@GMAIL.COM'
        user = get_user_model().objects.create_user(
            email=email,
            password='pass123'
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error."""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None,
                password='pass123'
            )

    def test_create_new_superuser(self):
        """Test creating a new superuser."""
        email = 'mdn1376@gmail.com'
        password = 'pass123'

        super_user = get_user_model().objects.create_superuser(
            email=email,
            password=password
        )

        self.assertEqual(super_user.email, email)
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
