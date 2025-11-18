from django.db import models

class Title(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Название"
        verbose_name_plural = "Названия"

class Announcement(models.Model):
    title = models.ForeignKey(Title, related_name='объявления', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='объявления/')
    description = models.TextField()
    link = models.URLField(blank=True, null=True, verbose_name="Ссылка")

    def __str__(self):
        return f"{self.title.name} - {self.id}"

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
