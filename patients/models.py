from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField  # Доп. пакет для телефонов

# добавить "phonenumber_field", в settings.py
from django.contrib.auth import get_user_model


User = get_user_model()


class Patient(models.Model):
    """
    Модель пациента, связанная с пользовательской моделью Django.
    Содержит персональные и контактные данные пациента.
    """

    class Gender(models.TextChoices):
        MALE = "M", "Мужской"
        FEMALE = "F", "Женский"

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="patient",
        verbose_name="Пользователь",
        help_text="Связанная учетная запись пользователя",
    )

    middle_name = models.CharField(
        verbose_name="Отчество",
        max_length=150,
        blank=True,  # Достаточно только blank (хранит пустую строку)
        help_text="Необязательное поле",
        validators=[MaxLengthValidator(150)],
    )

    birth_date = models.DateField(
        verbose_name="Дата рождения", help_text="Формат: ДД.ММ.ГГГГ"
    )

    gender = models.CharField(
        verbose_name="Пол", max_length=1, choices=Gender.choices, default=Gender.MALE
    )

    phone = PhoneNumberField(
        verbose_name="Телефон",
        blank=True,
        region="RU",
        help_text="Формат: +7XXXXXXXXXX",
    )

    is_active = models.BooleanField(
        verbose_name="Активный пациент",
        default=True,
        help_text="Отметьте, если пациент продолжает наблюдаться",
    )

    created_at = models.DateTimeField(
        verbose_name="Дата создания", auto_now_add=True, editable=False
    )

    last_update = models.DateTimeField(
        verbose_name="Последнее обновление", auto_now=True, editable=False
    )

    class Meta:
        verbose_name = "Пациент"
        verbose_name_plural = "Пациенты"
        # ordering = ["user__last_name", "user__first_name", "middle_name"]

        # indexes = [
        #     models.Index(fields=["user__last_name", "user__first_name"]),
        #     models.Index(fields=["birth_date"]),
        #     models.Index(fields=["is_active"]),
        # ]
        constraints = [
            models.UniqueConstraint(
                fields=["user"],
                name="unique_patient_user",
                violation_error_message="Пациент уже привязан к этому пользователю",
            )
        ]

    def __str__(self):
        return f"{self.user.last_name} {self.user.first_name} {self.middle_name or ' '}"

    @property
    def full_name(self) -> str:
        """Полное ФИО пациента"""
        return str(self)

    @property
    def age(self) -> int:
        """Вычисляет возраст пациента на текущую дату"""
        today = timezone.now().date()
        born = self.birth_date
        # Если день рождения ещё не наступил (сравнение True → 1), вычитаем 1
        # Если день рождения уже прошёл (сравнение False → 0), не вычитаем
        return (
            today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        )

    def save(self, *args, **kwargs):
        """Автоматическая нормализация данных перед сохранением"""
        if self.middle_name:
            self.middle_name = self.middle_name.strip().title()
        super().save(*args, **kwargs)


class MedicalCard(models.Model):
    """Медицинская карта пациента с клиническими данными"""

    patient = models.OneToOneField(
        Patient,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="medical_card",
        verbose_name="Пациент",
        help_text="Связанная запись пациента",
    )

    diagnosis = models.TextField(
        verbose_name="Основной диагноз",
        blank=True,
        default="",
        validators=[MaxLengthValidator(1000)],
        help_text="Максимум 1000 символов",
    )

    allergies = models.TextField(
        verbose_name="Аллергические реакции",
        blank=True,
        default="",
        help_text="Перечислите аллергены и реакции",
    )

    anamnesis = models.TextField(
        verbose_name="Анамнез",
        blank=True,
        default="",
        help_text="История болезни и жизни пациента",
    )

    last_medical_check = models.DateField(
        verbose_name="Дата последнего осмотра", blank=True, null=True
    )

    class Meta:
        verbose_name = "Медицинская карта"
        verbose_name_plural = "Медицинские карты"
        ordering = ["-last_medical_check"]

    def __str__(self):
        return f"Медкарта пациента: {self.patient.full_name}"

    @property
    def has_allergies(self) -> bool:
        """Проверяет наличие аллергий у пациента"""
        return bool(self.allergies and self.allergies.strip())

    @property
    def last_check_years(self) -> float:
        """Возвращает сколько лет прошло с последнего осмотра"""
        if not self.last_medical_check:
            return float("inf")
        delta = timezone.now().date() - self.last_medical_check
        return delta.days / 365.25


class HealthIndicator(models.Model):  # Модель медицинских показателей
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="health_indicators"
    )
    indicator_type = models.CharField(
        max_length=100,
        verbose_name="Тип показателя",
        help_text="Например: Артериальное давление, Вес",
    )
    value = models.FloatField(verbose_name="Значение")
    date_recorded = models.DateTimeField(verbose_name="Дата измерения")
    notes = models.TextField(blank=True, default="", verbose_name="Примечания")

    class Meta:
        verbose_name = "Медицинский показатель"
        verbose_name_plural = "Медицинские показатели"
        ordering = ["-date_recorded"]
        indexes = [
            models.Index(fields=["indicator_type"]),
        ]

    def __str__(self):
        return f"{self.indicator_type}: {self.value} ({self.patient})"
