from django.db import models

class Title(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок блока"
    )

    class Meta:
        verbose_name = "Блок оповещений"
        verbose_name_plural = "Блоки оповещений"
        ordering = ["id"]

    def __str__(self):
        return self.title


class Description(models.Model):
    section = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name="description",
        verbose_name="Блок оповещений"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True
    )
    image = models.ImageField(
        upload_to="notifications/",
        verbose_name="Изображение",
        blank=True
    )

    class Meta:
        verbose_name = "Оповещение"
        verbose_name_plural = "Оповещения"
        ordering = ["id"]

    def __str__(self):
        return self.title
