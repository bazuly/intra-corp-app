from django.test import TestCase, Client
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import EducationModel
from django.urls import reverse


class EducationAppTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.education_content = EducationModel.objects.create(
            title='test title',
            content='main_content',
        )

    def test_education_data_view(self):
        url = reverse('education_app:education_content')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'education_list.html')

    def test_education_data_detail_view(self):
        url = self.client.get(
            reverse('education_app:education_content_detail',
                    args=[self.education_content.id])
        )
        self.assertEqual(url.status_code, 200)
        self.assertTemplateUsed(url, 'education_detail.html')
        self.assertEqual(url.context['education_item'], self.education_content)
