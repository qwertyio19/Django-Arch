from django.db import models
from ckeditor.fields import RichTextField

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
