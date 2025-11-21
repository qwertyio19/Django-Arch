# app/council/models.py
from django.db import models
from .utils import file_to_html


class CouncilSection(models.Model):
    # Категория / раздел "Сельского кенеша"
    title = models.CharField(
        max_length=255,
        verbose_name="Бөлүм аталышы"
    )
    detail_title = models.CharField(
        max_length=255,
        verbose_name="Толук аталышы",
        blank=True
    )

    class Meta:
        verbose_name = "Айылдык кеңеш бөлүмү"
        verbose_name_plural = "Айылдык кеңеш бөлүмдөрү"
        ordering = ["id"]

    def __str__(self):
        return self.title


class CouncilDocument(models.Model):
    # Материал/документ внутри раздела
    section = models.ForeignKey(
        CouncilSection,
        on_delete=models.CASCADE,
        related_name="documents",
        verbose_name="Бөлүм"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Документтин аталышы"
    )
    description = models.TextField(
        verbose_name="Документтин сүрөттөлүшү",
        blank=True
    )
    file = models.FileField(
        upload_to="council_docs/",
        verbose_name="Файл (DOCX/PDF)"
    )
    content_html = models.TextField(
        verbose_name="Документтин HTML түрү",
        blank=True
    )

    class Meta:
        verbose_name = "Айылдык кеңеш документи"
        verbose_name_plural = "Айылдык кеңеш документтери"
        ordering = ["id"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Биринчи ирет сактайбыз – файл диске түшсүн
        super().save(*args, **kwargs)

        # Файлдан HTML чыгарып алабыз
        html = file_to_html(self.file)
        if html and html != self.content_html:
            self.content_html = html
            super().save(update_fields=["content_html"])
