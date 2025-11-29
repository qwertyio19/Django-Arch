from django.db import models
from .utils import file_to_html


class CouncilSection(models.Model):
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
        verbose_name = "Айылдык кеңеш бөлүм түрү"
        verbose_name_plural = "Айылдык кеңеш бөлүмүнүн түрлөрү"
        ordering = ["id"]

    def __str__(self):
        return self.title



class CouncilDocument(models.Model):
    section = models.ForeignKey(
        CouncilSection,
        on_delete=models.SET_NULL,
        null=True,
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
        super().save(*args, **kwargs)

        html = file_to_html(self.file)
        if html and html != self.content_html:
            self.content_html = html
            super().save(update_fields=["content_html"])


class Deputies(models.Model):
    section = models.ForeignKey(
        CouncilSection,
        on_delete=models.SET_NULL,
        null=True,
        related_name="deputies",
        verbose_name="Бөлүм"
    )
    position = models.CharField(
        max_length=255,
        verbose_name="Депутаттын кызматы"
    )
    name = models.CharField(
        max_length=255,
        verbose_name="Депутаттын аты-жөнү"
    )
    contact = models.CharField(
        max_length=255,
        verbose_name="Байланыш маалыматтары",
        default='Байланыш маалыматтары'
    )
    real_contact = models.CharField(
        max_length=255,
        verbose_name="Чыныгы байланыш маалыматтары",
        blank=True
    )
    district = models.CharField(
        max_length=255,
        default='Шайлоо округуна тиешелүүлүгү',
        verbose_name="Депутаттын шайланган аймагы",
    )
    real_district = models.CharField(
        max_length=255,
        verbose_name="Чыныгы депутаттын шайланган аймагы",
    )
    faction = models.CharField(
        max_length=255,
        default='Фракцияга тиешелүүлүгү',
        verbose_name="Фракция",
    )
    real_faction = models.CharField(
        max_length=255,
        verbose_name="Чыныгы фракция",
    )
    role = models.CharField(
        max_length=255,
        default='Кайсы комиссияга тиешелүү жана кайсы кызматты ээлейт',
        verbose_name="Депутаттын ролу"
    )
    real_role = models.CharField(
        max_length=255,
        verbose_name="Чыныгы депутаттын ролу"
    )
    image = models.ImageField(
        upload_to='deputies/',
        verbose_name="Депутаттын сүрөтү"
    )


    class Meta:
        verbose_name = "Айылдык кеңеш депутаты"
        verbose_name_plural = "Айылдык кеңеш депутаттары"
        ordering = ["id"]

    def __str__(self):
        return self.name
    


class Commission(models.Model):
    section = models.ForeignKey(
        CouncilSection,
        on_delete=models.SET_NULL,
        null=True,
        related_name="commission",
        verbose_name="Бөлүм"
    )
    position = models.CharField(
        max_length=255,
        verbose_name="Депутаттын кызматы"
    )
    name = models.CharField(
        max_length=255,
        verbose_name="Депутаттын аты-жөнү"
    )
    contact = models.CharField(
        max_length=255,
        verbose_name="Байланыш маалыматтары",
        default='Байланыш маалыматтары'
    )
    real_contact = models.CharField(
        max_length=255,
        verbose_name="Чыныгы байланыш маалыматтары",
        blank=True
    )
    district = models.CharField(
        max_length=255,
        default='Шайлоо округуна тиешелүүлүгү',
        verbose_name="Депутаттын шайланган аймагы",
    )
    real_district = models.CharField(
        max_length=255,
        verbose_name="Чыныгы депутаттын шайланган аймагы",
    )
    faction = models.CharField(
        max_length=255,
        default='Фракцияга тиешелүүлүгү',
        verbose_name="Фракция",
    )
    real_faction = models.CharField(
        max_length=255,
        verbose_name="Чыныгы фракция",
    )
    role = models.CharField(
        max_length=255,
        default='Кайсы комиссияга тиешелүү жана кайсы кызматты ээлейт',
        verbose_name="Депутаттын ролу"
    )
    real_role = models.CharField(
        max_length=255,
        verbose_name="Чыныгы депутаттын ролу"
    )
    image = models.ImageField(
        upload_to='deputies/',
        verbose_name="Депутаттын сүрөтү"
    )


    class Meta:
        verbose_name = "Туруктуу комиссиянын тизмеси"
        verbose_name_plural = "Туруктуу комиссиянын тизмелери"
        ordering = ["id"]

    def __str__(self):
        return self.name
