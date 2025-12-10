from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class TypeTitle(models.Model):
    type = models.CharField(
        max_length=500,
        verbose_name='Түрү'
    )
    title = models.CharField(
        max_length=500,
        verbose_name='Аталышы'
    )

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Айыл аймагынын түрү'
        verbose_name_plural = 'Айыл аймагынын түрлөрү'


class Data(models.Model):
    type_title = models.ForeignKey(
        TypeTitle,
        on_delete=models.SET_NULL,
        null=True,
        related_name='data',
        verbose_name='Түрү'
    )
    date = models.DateField(
        verbose_name='Жылы'
    )
    description = RichTextField(
        verbose_name='Түшүндүрмөсү'
    )

    def __str__(self):
        return f'{self.type_title} - {self.date}'

    class Meta:
        verbose_name = 'Айыл аймагы жөнүндө'
        verbose_name_plural = 'Айыл аймагы жөнүндө'


class DataImage(models.Model):
    data = models.ForeignKey(
        Data,
        related_name='images',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Маалыматтар'
    )
    image = models.ImageField(
        upload_to='report',
        verbose_name='Сүрөт'
    )

    def __str__(self):
        return f'{self.data} - {self.id}'

    class Meta:
        verbose_name = 'Сүрөт'
        verbose_name_plural = 'Сүрөттөр'