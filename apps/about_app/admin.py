from django.contrib import admin
from .models import AboutEmployeeModel, JobModel, ReferenceBookModel, WorkPlace

admin.site.register(AboutEmployeeModel)
admin.site.register(JobModel)
admin.site.register(ReferenceBookModel)
admin.site.register(WorkPlace)