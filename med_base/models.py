from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.core.validators import MinLengthValidator, MaxLengthValidator
from patients.models import Patient


class Examination(models.Model):
    """Модель инструментального исследования"""

    class ExaminationType(models.TextChoices):
        ULTRASOUND = 'ultrasound', 'УЗИ'
        MRI = 'mri', 'МРТ'
        CT = 'ct', 'КТ'
        XRAY = 'xray', 'Рентген'

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="examinations",
        verbose_name="Пациент",
    )
    examination_type = models.CharField(
        max_length=20,
        choices=ExaminationType.choices,
        verbose_name='Тип исследования'
    )
    name = models.CharField(
        max_length=100,
        verbose_name="Область исследования",
        help_text="например: сердца, ОБП",
    )
    examination_date = models.DateField(
        default=timezone.now,
        verbose_name='Дата проведения'
    )
    image = models.ImageField(
        upload_to="examinations/%Y/%m/",
        verbose_name="Изображение",
    )
    notes = models.TextField(
        blank=True, default="", verbose_name="Примечания", help_text="заметки"
    )

    class Meta:
        verbose_name = "Инструментальное исследование"
        verbose_name_plural = "Инструментальные исследования"
        ordering = ["patient", "name", "-examination_date"]
        indexes = [
            models.Index(fields=['examination_date']),
            models.Index(fields=['patient', 'examination_type']),
        ]

    def __str__(self):
        return f"{self.patient} {self.examination_type} {self.name} от {self.examination_date}"

    def get_absolute_url(self):
        return reverse('examination_detail', kwargs={'pk': self.pk})


class LaboratoryTest(models.Model):
    """Модель вида лабораторного исследования"""

    class TestType(models.TextChoices):
        BIOCHEMICAL_BLOOD = "biochemical-blood", "Биохимия крови"
        COMPLETE_BLOOD_COUNT = "complete-blood-count", "Общий анализ крови"
        GENERAL_URINE_ANALYSIS = "general-urine-analysis", "Общий анализ мочи"

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="laboratory_tests",
        verbose_name="Пациент",
    )
    test_type = models.CharField(
        max_length=30,
        choices=TestType.choices,
        default=TestType.BIOCHEMICAL_BLOOD,
        verbose_name="Вид анализа",
    )
    examination_date = models.DateField(verbose_name="Дата проведения")

    class Meta:
        verbose_name = "Группа лабораторного анализа"
        verbose_name_plural = "Группа лабораторных анализов"
        ordering = ["patient", "-examination_date"]

    def __str__(self):
        return f"{self.patient} {self.test_type} от {self.examination_date}"


class TestParameter(models.Model):
    """Модель параметра и результата лабораторного анализа"""

    test = models.ForeignKey(
        LaboratoryTest,
        on_delete=models.PROTECT,
        related_name='parameters',
        verbose_name='Группа анализов'
    )
    name = models.CharField(max_length=100, verbose_name="Параметр")
    value = models.CharField(max_length=10, verbose_name="Значение")
    unit = models.CharField(
        max_length=30, blank=True, verbose_name="Единицы измерения",
    )
    normal_range = models.CharField(
        max_length=30, blank=True, verbose_name="Референсные значения"
    )
    is_normal = models.BooleanField(default=True, verbose_name="В норме")
    notes = models.TextField(
        blank=True,
        default='',
        verbose_name='Комментарии'
    )

    class Meta:
        verbose_name = "Параметр анализа, значения"
        verbose_name_plural = "Параметры анализов, значения"
        ordering = ["name"]

    def __str__(self):
        return f'{self.name}: {self.value}{" " + self.unit if self.unit else ""}'
