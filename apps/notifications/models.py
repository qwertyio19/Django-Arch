from django.db import models


class Title(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Название"
        verbose_name_plural = "Названия"


class Announcement(models.Model):
    title = models.ForeignKey(
        Title,
        related_name='announcements',  
        on_delete=models.CASCADE,
        verbose_name="Название"
    )
    image = models.ImageField(upload_to='announcements/', verbose_name="Изображение")
    description = models.TextField(verbose_name="Описание")
    link = models.URLField(blank=True, null=True, verbose_name="Ссылка")

    def __str__(self):
        return f"{self.title.name} - {self.id}"

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
