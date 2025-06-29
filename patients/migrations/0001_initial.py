# Generated by Django 5.2.2 on 2025-06-25 16:40

import django.core.validators
import django.db.models.deletion
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="HealthIndicator",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "indicator_type",
                    models.CharField(
                        help_text="Например: Артериальное давление, Вес",
                        max_length=100,
                        verbose_name="Тип показателя",
                    ),
                ),
                ("value", models.FloatField(verbose_name="Значение")),
                ("date_recorded", models.DateTimeField(verbose_name="Дата измерения")),
                (
                    "notes",
                    models.TextField(blank=True, default="", verbose_name="Примечания"),
                ),
            ],
            options={
                "verbose_name": "Медицинский показатель",
                "verbose_name_plural": "Медицинские показатели",
                "ordering": ["-date_recorded"],
            },
        ),
        migrations.CreateModel(
            name="Patient",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        help_text="Связанная учетная запись пользователя",
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name="patient",
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
                (
                    "middle_name",
                    models.CharField(
                        blank=True,
                        help_text="Необязательное поле",
                        max_length=150,
                        validators=[django.core.validators.MaxLengthValidator(150)],
                        verbose_name="Отчество",
                    ),
                ),
                (
                    "birth_date",
                    models.DateField(
                        help_text="Формат: ДД.ММ.ГГГГ", verbose_name="Дата рождения"
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Мужской"), ("F", "Женский")],
                        default="M",
                        max_length=1,
                        verbose_name="Пол",
                    ),
                ),
                (
                    "phone",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True,
                        help_text="Формат: +7XXXXXXXXXX",
                        max_length=128,
                        region="RU",
                        verbose_name="Телефон",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Отметьте, если пациент продолжает наблюдаться",
                        verbose_name="Активный пациент",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "last_update",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Последнее обновление"
                    ),
                ),
            ],
            options={
                "verbose_name": "Пациент",
                "verbose_name_plural": "Пациенты",
            },
        ),
        migrations.CreateModel(
            name="MedicalCard",
            fields=[
                (
                    "patient",
                    models.OneToOneField(
                        help_text="Связанная запись пациента",
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name="medical_card",
                        serialize=False,
                        to="patients.patient",
                        verbose_name="Пациент",
                    ),
                ),
                (
                    "diagnosis",
                    models.TextField(
                        blank=True,
                        default="",
                        help_text="Максимум 1000 символов",
                        validators=[django.core.validators.MaxLengthValidator(1000)],
                        verbose_name="Основной диагноз",
                    ),
                ),
                (
                    "allergies",
                    models.TextField(
                        blank=True,
                        default="",
                        help_text="Перечислите аллергены и реакции",
                        verbose_name="Аллергические реакции",
                    ),
                ),
                (
                    "anamnesis",
                    models.TextField(
                        blank=True,
                        default="",
                        help_text="История болезни и жизни пациента",
                        verbose_name="Анамнез",
                    ),
                ),
                (
                    "last_medical_check",
                    models.DateField(
                        blank=True, null=True, verbose_name="Дата последнего осмотра"
                    ),
                ),
            ],
            options={
                "verbose_name": "Медицинская карта",
                "verbose_name_plural": "Медицинские карты",
                "ordering": ["-last_medical_check"],
            },
        ),
        migrations.AddConstraint(
            model_name="patient",
            constraint=models.UniqueConstraint(
                fields=("user",),
                name="unique_patient_user",
                violation_error_message="Пациент уже привязан к этому пользователю",
            ),
        ),
        migrations.AddField(
            model_name="healthindicator",
            name="patient",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="health_indicators",
                to="patients.patient",
            ),
        ),
        migrations.AddIndex(
            model_name="healthindicator",
            index=models.Index(
                fields=["indicator_type"], name="patients_he_indicat_b7e364_idx"
            ),
        ),
    ]
