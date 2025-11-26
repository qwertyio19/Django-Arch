from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone

class CartModel(models.Model):
    title = models.CharField(max_length=155, verbose_name="ФИО")
    description = RichTextField(blank=True, verbose_name="Сөзү (глава)")
    image = models.ImageField(blank=True, null=True, verbose_name="Главанын сүрөтү")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Башчынын сөздөрү"
        verbose_name_plural = "Башчынын сөздөрү"
    

class HeadlinesModel(models.Model):
    KokBelLocalGovernment = models.CharField(max_length=255, verbose_name="Көк-Бел жергиликтүү өз алдынча башкаруусу")
    Announcements = models.CharField(max_length=255, verbose_name="Жарыялар")
    Latestannouncements = models.CharField(max_length=255, verbose_name="Акыркы жарыялар")
    Anticorruptionmeasures = models.CharField(max_length=255, verbose_name="Антикоррупциялык чаралар")
    Governmentportal = models.CharField(max_length=255, verbose_name="Кыргыз Республикасынын мамлекеттик порталы")
    Jobs = models.CharField(max_length=255, verbose_name="Вакансиялар")

    def __str__(self):
        return self.KokBelLocalGovernment

    class Meta:
        verbose_name = "Башкы беттеги заголовок"
        verbose_name_plural = "Башкы беттеги заголовоктор"


class VisitorStatistics(models.Model):
    """Простая модель для подсчета посетителей сайта"""
    date = models.DateField(
        unique=True, 
        verbose_name='Дата', 
        default=timezone.now
    )
    visitors = models.IntegerField(
        default=0, 
        verbose_name='Посетители'
    )
    
    class Meta:
        verbose_name = 'Статистика посещений'
        verbose_name_plural = 'Статистика посещений'
    
    def __str__(self):
        return f"Статистика за {self.date}: {self.visitors} посетителей"
        
    @classmethod
    def get_total_statistics(cls):
        stats = cls.objects.aggregate(
            total_visitors=models.Sum('visitors')
        )
        return {
            'total_visitors': stats['total_visitors'] or 0
        }


class Footer(models.Model):
    """Модель для футера и хедера сайта"""
    logo = models.ImageField(
        upload_to='images/', 
        blank=True, null=True, 
        verbose_name="Логотип"
    )
    navigation = models.CharField(
        max_length=200,
        default='Навигация',
        verbose_name="Навигация",
    )
    home = models.CharField(
        max_length=100,
        default='Башкы',
        verbose_name="Башкы бет",
    )
    aiyl_aimagy = models.CharField(
        max_length=100,
        default='Айыл Аймагы',
        verbose_name="Айыл Аймагы",
    )
    aiyl_okmotu = models.CharField(
        max_length=100,
        default='Айыл Өкмөтү',
        verbose_name="Айыл Өкмөтү",
    )
    aiyldyk_kenesh = models.CharField(
        max_length=100,
        default='Айылдык Кеңеш',
        verbose_name="Айылдык Кеңеш",
    )
    obrashenie_gragdan = models.CharField(
        max_length=100,
        default='Жарандардын кайрылуулары',
        verbose_name="Жарандардын кайрылуулары",
    )
    novosti = models.CharField(
        max_length=100,
        default='Жаңылыктар',
        verbose_name="Жаңылыктар",
    )
    obiavlenie = models.CharField(
        max_length=100,
        default='Жарнамалар',
        verbose_name="Жарнамалар",
    )
    statistic_title = models.CharField(
        max_length=100,
        default='Статистика',
        verbose_name="Статистиканын аталышы",
        help_text="Статистика бөлүмүнүн аталышы"
    )
    show_statistics = models.BooleanField(
        default=True,
        verbose_name="Статистиканы көрсөтүү"
    )
    title_address = models.CharField(
        max_length=50,
        default="Адрес",
        verbose_name="Адрес",
        help_text="Колонтитулда көрсөтүлө турган дарек сөзү"
    )
    address = models.CharField(
        max_length=50,
        verbose_name="Адрес",
        help_text="Колонтитулда көрсөтүлө турган дарек"
    )
    title_phone = models.CharField(
        max_length=50,
        default="Телефон",
        verbose_name="Телефон",
        help_text="Колонтитулда көрсөтүлө турган телефон сөзү"
    )
    phone = models.CharField(
        max_length=50,
        verbose_name="Телефон",
        help_text="Колонтитулда көрсөтүлө турган телефон номери"
    )
    soicial_media = models.CharField(
        max_length=50,
        default="соц-тармак",
        verbose_name="соц-тармак"
    )
    facebook = models.URLField(
        blank=True,
        verbose_name="Социалдык тармак",
        help_text="Facebook шилтемеңизди киргизиңиз"
    )
    
    def __str__(self):
        return "Хэдерлер жана футерлер"
    
    class Meta:
        verbose_name = 'Хэдер жана футер'
        verbose_name_plural = 'Хэдерлер жана футерлер'


class PagetitlesModel(models.Model):
    ruraldistrict = models.CharField(max_length=255, verbose_name='Айылдык округ', default='Айылдык округ')
    ruralcouncil = models.CharField(max_length=255, verbose_name='Айыл өкмөт', default='Айыл өкмөт')
    villagecouncil = models.CharField(max_length=255, verbose_name='Айылдык кеңеш', default='Айылдык кеңеш')
    news = models.CharField(max_length=255, verbose_name='Жанылыктар', default='Жанылыктар')
    announcement = models.CharField(max_length=255, verbose_name='Жарнамалар', default='Жарнамалар')
