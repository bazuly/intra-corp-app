from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from apps.about_app.models import JobModel
from .models import VacationModel, VacancyModel, VacancyRequestModel

from users.models import User


class HrAppTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.job = JobModel.objects.create(
            job_title='Водитель-экспедитор'
        )
        self.vacancy = VacancyModel.objects.create(
            vacancy_name='Test Vacancy',
            salary='Test salary',
            short_description='Test Description',
            content='Test content',
            uploaded_at='2024-01-01',
        )
        self.vacation_data = {
            'name': 'test_vacation',
            'vacation_date_start': '2024-05-05',
            'vacation_date_end': '2024-06-06',
            'status_confirm': 'На согласовании',
            'job': self.job,
            'vacation_type': 'Оплаичваемый отпуск'
        }
        self.vacancy_response_data = VacancyRequestModel.objects.create(
            name='test name',
            contact='test contact info',
            covering_letter='test covering letter',
            vacancy='vacancy name'
        )
        self.vacancy_response_data_dict = {
            'name': 'Test User',
            'contact': 'test@example.com',
            'covering_letter': 'This is a test covering letter.',
            'vacancy': 'vacancy name'
        }

    def test_upload_vacation_data_view(self):
        url = reverse('hr_app:vacation_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'list_vacation.html')

    def test_upload_vacation_data(self):
        data = self.vacation_data
        file_content = b"file content"
        file = SimpleUploadedFile('test_file.jpg', file_content)
        data['vacation_file'] = file
        response = self.client.post(
            reverse('hr_app:vacation_upload'), data, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_search_vacation_data(self):
        VacationModel.objects.create(
            name='test_name',
            vacation_date_start='2024-05-05',
            vacation_date_end='2024-06-06',
            job=self.job,
            vacation_type='Оплачиваемый отпуск'
        )
        expected_search_result = VacationModel.objects.filter(name='test_name')
        response = self.client.get(
            reverse('hr_app:search_vac_data'), {'q': 'test_name'})
        self.assertEqual(response.status_code, 200)
        actual_result = response.context['vac_data']
        self.assertQuerySetEqual(expected_search_result, actual_result)

    def test_vacancy_data_view(self):
        url = reverse('hr_app:vacancy_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vacancy_list.html')

    def test_vacancy_detail_data_view(self):
        url = self.client.get(
            reverse('hr_app:vacancy_detail', args=[self.vacancy.id])
        )
        self.assertEqual(url.status_code, 200)
        self.assertTemplateUsed(url, 'vacancy_detail.html')
        self.assertEqual(url.context['vacancy_item'], self.vacancy)

    def test_requset_to_vacancy(self):
        data = self.vacancy_response_data_dict
        file_content = b"file content"
        resume_file = SimpleUploadedFile('resume_file.jpg', file_content)
        data['resume_upload'] = resume_file
        response = self.client.post(
            reverse('hr_app:response_to_vacancy',
                    args=[self.vacancy_response_data.id]), data, follow=True)
        self.assertEqual(response.status_code, 200)
