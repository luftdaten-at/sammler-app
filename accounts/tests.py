from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve


class CustomUserTests(TestCase):
    
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='tester',
            email='tester@luftdaten.at',
            password='SaubereLuft2021'
        )
        self.assertEqual(user.username, 'tester')
        self.assertEqual(user.email, 'tester@luftdaten.at')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username ='superadmin',
            email='superadmin@luftdaten.at',
            password='SaubereLuftAdmin2021'
        )
        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'superadmin@luftdaten.at')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SignupTests(TestCase):
    
    username = 'tester'
    email = 'tester@luftdaten.at'
    
    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)
    
    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Sign Up')
    
    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(
            self.username, self.email
        )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)