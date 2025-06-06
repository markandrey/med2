from django.contrib import admin
from .models import Group, Test, TestName

admin.site.register(Group)
admin.site.register(Test)
admin.site.register(TestName)
