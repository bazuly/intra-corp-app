from django import forms
from .models import AboutEmployeeModel, JobModel, ReferenceBookModel, WorkPlace


class AboutEmployeeForm(forms.ModelForm):
    class Meta:
        model = AboutEmployeeModel
        fields = [
            'name',
            'content',
            'photo'
        ]


class JobModelForm(forms.ModelForm):
    class Meta:
        model = JobModel
        fields = [
            'name'
        ]


class ReferenceBookModelForm(forms.ModelForm):
    class Meta:
        model = ReferenceBookModel
        fields = [
            'name',
            'job',
            'additional_number',
            'additional_info'
        ]


class WorkPlace(forms.ModelForm):
    class Meta:
        model = WorkPlace
        fields = [
            'work_place'
        ]
