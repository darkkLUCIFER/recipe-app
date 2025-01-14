from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@gmail.com',
            password='pass123',
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test@gmail.com',
            password='test123',
            name='Test User',
        )

    def test_users_listed(self):
        """Test that users are listed on user page"""
        url = reverse('admin:accounts_user_changelist')
        response = self.client.get(url)

        self.assertContains(response, self.user.name)
        self.assertContains(response, self.user.email)

    def test_user_change_page(self):
        """Test that the user edit page works."""
        url = reverse('admin:accounts_user_change', args=[self.user.id])

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_crete_user_page(self):
        """Test that the user create page works."""
        url = reverse('admin:accounts_user_add')

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
