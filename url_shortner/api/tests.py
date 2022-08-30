from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import urlShortener

class ShortnerTests(APITestCase):
    def test_create_short_url(self):
        """
        Ensure we can create a new short url.
        """
        url = reverse('shorten')
        data = {'longurl': 'www.google.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['shorturl'].split(r"/")[-1]), 6)
        self.assertEqual(urlShortener.objects.count(), 1)
        self.assertEqual(urlShortener.objects.get().longurl, 'www.google.com')
        self.assertEqual(urlShortener.objects.get().clicks, 0)

    def test_click_short_url(self):
        """
        Ensure click method update count.
        """
        url = reverse('shorten')
        data = {'longurl': 'www.google.com'}
        response = self.client.post(url, data, format='json')
        shorturl = response.data['shorturl']
        # click it
        url = reverse('clicks')
        data = {'shorturl': shorturl}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['clicks'], 1)
        self.assertEqual(urlShortener.objects.count(), 1)
        self.assertEqual(urlShortener.objects.get().longurl, 'www.google.com')
        self.assertEqual(urlShortener.objects.get().clicks, 1)

    def test_multiple_calls_to_shorten_same_url_gives_different_short_url(self):
        """
        As in the name
        """
        url = reverse('shorten')
        data = {'longurl': 'www.google.com'}
        response = self.client.post(url, data, format='json')
        shorturl = response.data['shorturl']

        url = reverse('shorten')
        data = {'longurl': 'www.google.com'}
        response = self.client.post(url, data, format='json')
        shorturl_next = response.data['shorturl']
        self.assertNotEquals(shorturl, shorturl_next)
        # and two rows now
        self.assertEqual(urlShortener.objects.count(), 2)

    def test_summary_returns_correct_table_and_values(self):
        """
        As in the name
        """
        url = reverse('summary')
        response = self.client.get(url,format='json')
        self.assertListEqual(response.data, [])

        #multiple queries
        url = reverse('shorten')
        run_for_n_times = 10 
        for x in range(0,run_for_n_times):
            data = {'longurl': 'www.google.com'}
            response = self.client.post(url, data, format='json')
            shorturl = response.data['shorturl']

        url = reverse('summary')
        response = self.client.get(url,format='json')
        self.assertTrue(len(response.data)==run_for_n_times)