from django.test import TestCase, Client
from django.urls import reverse
from .models import JobModel, ReferenceBookModel

from django.contrib.auth.models import User


class AboutAppTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
        )
        self.job = JobModel.objects.create(
            job_title='Водитель-экспедитор'
        )
        self.reference_data = ReferenceBookModel.objects.create(
            name='Test Book 1',
            job=self.job,
            additional_number='614',
            additional_info='test additional info',
        )

    def test_upload_vacation_data_view(self):
        url = reverse('about_app:page_about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'list_about_major_employer.html')

    def test_reference_book_list_view(self):
        self.client.force_login(self.user)
        self.assertTrue(self.user.is_authenticated)
        url = reverse('about_app:reference_book_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'list_reference_book.html')
        self.assertContains(response, 'Test Book 1')

    def test_search_reference_data(self):
        self.client.force_login(self.user)
        self.assertTrue(self.user.is_authenticated)
        ReferenceBookModel.objects.create(
            name='Test Book 1',
            job=self.job,
            additional_number='614',
            additional_info='test additional info',
        )
        expected_search_data = ReferenceBookModel.objects.filter(
            name='Test Book 1')
        response = self.client.get(
            reverse('about_app:search_data_reference_book'),
            {'q': 'test_name'})
        self.assertEqual(response.status_code, 200)
        actual_result = response.context['reference_book_data']
        self.assertQuerySetEqual(expected_search_data, actual_result)
