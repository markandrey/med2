from django.contrib import admin
from patients.models import Patient, MedicalCard, HealthIndicator

admin.site.register(Patient)
admin.site.register(MedicalCard)
admin.site.register(HealthIndicator)

# тонкая настройка отображения админ-панели
# @admin.register()