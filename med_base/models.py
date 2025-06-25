from django.db import models
from django.urls import reverse
from django.utils import timezone

from patients.models import Patient


class Examination(models.Model):
    class ExaminationType(models.TextChoices):
        ANALYSIS = 'analysis', 'Лабораторный анализ'
        DIAGNOSTIC = 'diagnostic', 'Диагностическое исследование'

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='examinations',
        verbose_name='Пациент'
    )
    examination_type = models.CharField(
        max_length=20,
        choices=ExaminationType.choices,
        default=ExaminationType.ANALYSIS,
        verbose_name='Тип исследования'
    )
    name = models.CharField(max_length=100, verbose_name='Название исследования')
    examination_date = models.DateTimeField(verbose_name='Дата проведения')
    notes = models.TextField(blank=True, default="", verbose_name='Примечания')

    class Meta:
        verbose_name = 'Исследование'
        verbose_name_plural = 'Исследования'
        ordering = ['-examination_date']
        indexes = [
            models.Index(fields=['examination_type']),
            models.Index(fields=['examination_date']),
        ]

    def __str__(self):
        return f'{self.patient} {self.name} от {self.examination_date}'

    def get_absolute_url(self):
        return reverse('examination_detail', args=[str(self.id)])


class AnalysisResult(models.Model):
    examination = models.OneToOneField(
        Examination,
        on_delete=models.CASCADE,
        related_name='analysis_result',
        verbose_name='Исследование',
        limit_choices_to={'examination_type': 'analysis'}
    )
    laboratory = models.CharField(max_length=30, blank=True, verbose_name='Лаборатория')

    class Meta:
        verbose_name = 'Результат анализа'
        verbose_name_plural = 'Результаты анализов'

    def __str__(self):
        return f'Результаты анализа {self.examination.name}'


class AnalysisParameter(models.Model):
    result = models.ForeignKey(
        AnalysisResult,
        on_delete=models.CASCADE,
        related_name='parameters',
        verbose_name='Результат анализа'
    )
    name = models.CharField(max_length=100, verbose_name='Параметр')
    value = models.CharField(max_length=10, verbose_name='Значение')
    unit = models.CharField(max_length=20, blank=True, verbose_name='Единицы измерения')
    normal_range = models.CharField(max_length=30, blank=True, verbose_name='Референсные значения')
    is_normal = models.BooleanField(default=True, verbose_name='В норме')

    class Meta:
        verbose_name = 'Параметр анализа'
        verbose_name_plural = 'Параметры анализов'
        ordering = ['name']

    def __str__(self):
        return f'{self.name}: {self.value}{" " + self.unit if self.unit else ""}'


class DiagnosticResult(models.Model):
    examination = models.OneToOneField(
        Examination,
        on_delete=models.CASCADE,
        related_name='diagnostic_result',
        verbose_name='Исследование',
        limit_choices_to={'examination_type': 'diagnostic'}
    )
    protocol = models.TextField(blank=True, default="", verbose_name='Текстовый протокол')
    conclusion = models.TextField(blank=True, default="", verbose_name='Заключение')

    class Meta:
        verbose_name = 'Результат диагностики'
        verbose_name_plural = 'Результаты диагностики'

    def __str__(self):
        return f'Результат {self.examination.name}'

class DiagnosticImage(models.Model):
    # Если пациент с ID=5 загружает файл "scan_2023.jpg", файл будет сохранён в:
    # media/diagnostics/5/scan_2023.jpg
    def upload_to_path(instance, filename):
        return f'diagnostics/{instance.result.examination.patient.id}/{filename}'

    result = models.ForeignKey(
        DiagnosticResult,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Результат исследования'
    )
    image = models.ImageField(upload_to=upload_to_path, verbose_name='Изображение')

    class Meta:
        verbose_name = 'Изображение исследования'
        verbose_name_plural = 'Изображения исследований'


class HealthIndicator(models.Model):  # Модель медицинских показателей
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='health_indicators')
    indicator_type = models.CharField(max_length=100, verbose_name='Тип показателя', help_text='Например: Артериальное давление, Вес')
    value = models.FloatField(verbose_name='Значение')
    date_recorded = models.DateTimeField(verbose_name='Дата измерения')
    notes = models.TextField(blank=True, default="", verbose_name='Примечания')

    class Meta:
        verbose_name = 'Медицинский показатель'
        verbose_name_plural = 'Медицинские показатели'
        ordering = ['-date_recorded']
        indexes = [
            models.Index(fields=['indicator_type']),
        ]

    def __str__(self):
        return f"{self.indicator_type}: {self.value} ({self.patient})"
