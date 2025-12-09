from django.db import models
from ckeditor.fields import RichTextField

from apps.kenesh.utils import file_to_html
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



class TitleAdministration(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Аталышы"
    )

    class Meta:
        verbose_name = "Айыл өкмөтүнүн темасы"
        verbose_name_plural = "Айыл өкмөтүнүн темалары"

    def __str__(self):
        return self.title



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



class Structure(models.Model):
    type = models.ForeignKey(
        TypeAdministration,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Түрү'
    )
    image = models.ImageField(
        upload_to='structure',
        verbose_name='Сүрөт'
    )

    def __str__(self):
        return f"Курулушу {self.pk}"

    class Meta:
        verbose_name = 'Курулуш'
        verbose_name_plural = 'Курулушу'



class Vacancy(models.Model):
    type = models.ForeignKey(
        TypeAdministration,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Түрү'
    )
    title = models.CharField(
        max_length=500,
        verbose_name='Аталышы'
    )
    description = RichTextField(
        verbose_name='Түшүндүрмөсү'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансиялар'



class AntiCorruptionMeasures(models.Model):
    type = models.ForeignKey(
        TypeAdministration,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Түрү'
    )
    common_title = models.ForeignKey(
        TitleAdministration,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Темасы'
    )
    title = models.CharField(
        max_length=500,
        default='Аталышы',
        verbose_name='Аталышы'
    )
    real_title = models.CharField(
        max_length=500,
        verbose_name='Аталышы'
    )
    description = models.CharField(
        max_length=500,
        default='Түшүндүрмөсү',
        verbose_name='Түшүндүрмөсү'
    )
    real_description = RichTextField(
        verbose_name='Түшүндүрмөсү'
    )
    image = models.ImageField(
        upload_to='anti_corrup_images/',
        verbose_name='Сүрөт',
        blank=True,
        null=True
    )
    file = models.FileField(
        upload_to="anti_corrup_docs/",
        verbose_name="Файл (DOCX/PDF)"
    )
    content_html = models.TextField(
        verbose_name="Документтин HTML түрү",
        blank=True
    )

    def __str__(self):
        return self.real_title
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        html = file_to_html(self.file)
        if html and html != self.content_html:
            self.content_html = html
            super().save(update_fields=["content_html"])

    class Meta:
        verbose_name = 'Коррупцияга каршы чара'
        verbose_name_plural = 'Коррупцияга каршы чаралар'



class Report(models.Model):
    type = models.ForeignKey(
        TypeAdministration,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Түрү'
    )
    common_title = models.ForeignKey(
        TitleAdministration,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Темасы'
    )
    title = models.CharField(
        max_length=500,
        verbose_name='Аталышы'
    )
    description = RichTextField(
        verbose_name='Түшүндүрмөсү'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Эсеп'
        verbose_name_plural = 'Эсептер'


class ReportImage(models.Model):
    report = models.ForeignKey(
        Report,
        related_name='images',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Эсеп'
    )
    image = models.ImageField(
        upload_to='report',
        verbose_name='Сүрөт'
    )

    def __str__(self):
        return f'{self.report.title} - {self.id}'

    class Meta:
        verbose_name = 'Сүрөт'
        verbose_name_plural = 'Сүрөттөр'