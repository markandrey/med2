from django.contrib import admin
from med_base.models import (
    Examination,
    AnalysisResult,
    AnalysisParameter,
    DiagnosticResult,
    DiagnosticImage,
    HealthIndicator,
)


admin.site.register(Examination)
admin.site.register(AnalysisResult)
admin.site.register(AnalysisParameter)
admin.site.register(DiagnosticResult)
admin.site.register(DiagnosticImage)
admin.site.register(HealthIndicator)
