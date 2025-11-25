from django.db import models
from ckeditor.fields import RichTextField

class TypeNotification(models.Model):
    type = models.CharField(
        max_length=255,
        verbose_name="Түрүнүн аталышы"
    )

    class Meta:
        verbose_name = "Жарнаманын түрү"
        verbose_name_plural = "Жарнамалардын түрү"

    def __str__(self):
        return self.type


class Notification(models.Model):
    types = models.ForeignKey(
        TypeNotification,
        on_delete=models.SET_NULL,
        null=True,
        related_name="notification",
        verbose_name="Жарнаманын түрү"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Аталышы"
    )
    description = RichTextField(
        verbose_name="Сүрөттөмө",
        blank=True
    )
    date = models.CharField(
        max_length=255,
        verbose_name="Күнү"
        )
    image = models.ImageField(
        upload_to="notifications/",
        verbose_name="Жарнаманын cүрөтү"
    )

    class Meta:
        verbose_name = "Жарнама"
        verbose_name_plural = "Жарнамалар"
        ordering = ["id"]

    def __str__(self):
        return self.title
        return self.title
