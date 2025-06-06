from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Group(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        ordering = ["name"]
        verbose_name = 'Группа анализов'
        verbose_name_plural = 'Группы анализов'

    def __str__(self):
        return self.name


class TestName(models.Model):
    name = models.CharField(max_length=250)
    group = models.ForeignKey(Group, on_delete=models.PROTECT)   # Обратная связь: group.testname_set

    class Meta:
        ordering = ["name"]
        verbose_name = 'Название анализа'
        verbose_name_plural = 'Название анализов'

    def __str__(self):
        return self.name


class Test(models.Model):
    value = models.DecimalField(max_digits=9, decimal_places=3)
    upper_limit = models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
    down_limit = models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
    date = models.DateField(default=timezone.now)
    patient = models.ForeignKey(User, on_delete=models.CASCADE)  # Обратная связь: user.test_set
    name = models.ForeignKey(TestName, on_delete=models.PROTECT)   # Обратная связь: testname.test_set

    class Meta:
        ordering = ["name", "-date"]
        verbose_name = 'Анализ'
        verbose_name_plural = 'Анализы'

    def __str__(self):
        return f'Анализ {self.name}'
    