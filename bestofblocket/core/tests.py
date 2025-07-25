from django.test import Client, TestCase


class TestURLsTestCase(TestCase):
    fixtures = ["testdata.json"]

    def setUp(self):
        self.client = Client()

    def test_get_index(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_get_detail_page(self):
        response = self.client.get("/945-ltt-olivgron-glastaklucka/")
        self.assertContains(response, "Avgas bristfällig upphängning")
        self.assertEqual(response.status_code, 200)
