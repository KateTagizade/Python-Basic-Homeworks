from django.test import TestCase

class TestServicesListView(TestCase):

    def test_response_status_code(self):
        response = self.client.get('/services')
        self.assertEqual(response.status_code, 200)

    def test_response_context(self):
        response = self.client.get('/services')
        self.assertIn('help_text', response.context)
        self.assertEqual(response.context['help_text'], 'хэлптекст')