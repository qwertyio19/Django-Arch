from django.db import models

class News(models.Model):
    """Жанылыктар модели"""
    name = models.CharField(
        max_length=250,
        verbose_name='жанылыктын аталышы',
        help_text='жанылыктын аталышын жазыныз'
    )
    description = models.TextField(
        blank=True,
        verbose_name='толук маалымат',
        help_text='жанылыктын толук маалыматы'
    )
    date = models.CharField(
        verbose_name='датасы',
        help_text='Жанылыктын датасы'
    )
    image = models.ImageField(
        upload_to='news/images/',
        verbose_name='сүрөт'
    )

    class Meta:
        verbose_name = 'Жанылык'
        verbose_name_plural = 'Жанылыклар'
    
    def __str__(self):
        return self.name