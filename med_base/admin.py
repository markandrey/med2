from django.contrib import admin
from med_base.models import (
    Examination,
    LaboratoryTest,
    TestParameter,
)


admin.site.register(Examination)
admin.site.register(LaboratoryTest)
admin.site.register(TestParameter)
