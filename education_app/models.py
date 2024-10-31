from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
import os


def upload_to(instance, filename):
    return os.path.join('education', instance.title, filename)


class EducationModel(models.Model):
    title = models.CharField(
        max_length=128,
        verbose_name='Название',
        null=False,
    )
    content = RichTextUploadingField()
    main_photo = models.FileField(
        upload_to=upload_to,
        null=True,
        blank=True
    )
    uploaded_at = models.DateTimeField(
        auto_now=True
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
