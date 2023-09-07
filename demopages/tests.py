from django.test import TestCase, Client


class IndexTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_git_index_endpoint(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'Hello, world!')
# Create your tests here.
