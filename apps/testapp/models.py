from django.db import models
from django_ckeditor_5.fields import CKEditor5Field



class TestModel(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )
    description = CKEditor5Field(
        verbose_name = "Описания",
        config_name="extends"
    )