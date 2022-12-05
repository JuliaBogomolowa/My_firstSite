from django.db import models

class Model1(models.Model):
    pole1 = models.CharField(max_length=45)

    class Meta:
        verbose_name = "Модель"
        verbose_name_plural = "Модели"

    def __str__(self):
        return str(self.pole1)

class Model2(models.Model):
    pole1 = models.CharField(max_length=45)


    class Meta:
        verbose_name = "Модель"
        verbose_name_plural = "Модели"

    def __str__(self):
        return str(self.pole1)




