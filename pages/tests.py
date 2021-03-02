from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomeView, ImpressumView


class HomeTests(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)
    
    def test_home_status_code(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_home_template(self):
        self.assertTemplateUsed(self.response, 'home.html')
    
    def test_home_contains_correct_html(self):
        self.assertContains(self.response, 'Home')
    
    def test_home_url_resolves_homeview(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomeView.as_view().__name__
        )


class ImpressumTests(SimpleTestCase):
    
    def setUp(self):
        url = reverse('impressum')
        self.response = self.client.get(url)
    
    def test_impressum_status_code(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_impressum_template(self):
        self.assertTemplateUsed(self.response, 'impressum.html')
    
    def test_impressum_contains_correct_html(self):
        self.assertContains(self.response, 'Impressum')
    
    def test_impressum_url_resolves_impressumview(self):
        view = resolve('/impressum/')
        self.assertEqual(
            view.func.__name__,
            ImpressumView.as_view().__name__
        )
