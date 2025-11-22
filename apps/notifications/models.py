from django.db import models

class Title(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Бөлүм аталышы"
    )

    class Meta:
        verbose_name = "Айылдык кеңеш жарыя"
        verbose_name_plural = "Айылдык кеңеш жарыялар"
        ordering = ["id"]

    def __str__(self):
        return self.title


class Description(models.Model):
    section = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name="documents",
        verbose_name="Айылдык кеңеш жарыя"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Айылдык кеңеш жарыясынын аталышы"
    )
    description = models.TextField(
        verbose_name="Айылдык кеңеш жарыясынын сүрөттөлүшү",
        blank=True
    )
    file = models.FileField(
        upload_to="notifications/",
        verbose_name="Айылдык кеңеш жарыясынын файлы (DOCX/PDF)"
    )
    content_html = models.TextField(
        verbose_name="Айылдык кеңеш жарыясынын HTML түрү",
        blank=True
    )

    class Meta:
        verbose_name = "Айылдык кеңеш жарыясынын маалыматы"
        verbose_name_plural = "Айылдык кеңеш жарыясынын маалыматтары"
        ordering = ["id"]

    def __str__(self):
        return self.title
