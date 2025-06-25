from django.contrib import admin
from patients.models import Patient, MedicalCard

admin.site.register(Patient)
admin.site.register(MedicalCard)

# тонкая настройка отображения админ-панели
# @admin.register()