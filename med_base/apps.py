from django.apps import AppConfig


class MedBaseConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "med_base"
    verbose_name = 'Обследования'
