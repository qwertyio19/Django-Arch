from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class TypeAdministration(models.Model):
    type = models.CharField(
        max_length=255,
        verbose_name="Айыл өкмөтүнүн түрүнүн аталышы"
    )

    class Meta:
        verbose_name = "Айыл өкмөтүнүн түрү"
        verbose_name_plural = "Айыл өкмөтүнүн түрлөрү"

    def __str__(self):
        return self.type



class Management(models.Model):
    type = models.ForeignKey(
        TypeAdministration,
        on_delete=models.SET_NULL,
        null=True,
        related_name="management",
        verbose_name="Айыл өкмөтүнүн түрү"
    )
    role = models.CharField(
        max_length=255,
        verbose_name="Кызматы",
        default="Кызматы"
    )
    full_name = models.CharField(
        max_length=500,
        verbose_name="Толук аты-жөнү"
    )
    reseptions = models.CharField(
        max_length=500,
        verbose_name="Кабыл алуу күнү жана убактысы"
    )
    image = models.ImageField(
        upload_to="management/",
        verbose_name="Сүрөтү"
    )

    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = "Айыл өкмөтүнүн жетекчилиги"
        verbose_name_plural = "Айыл өкмөтүнүн жетекчилиги"