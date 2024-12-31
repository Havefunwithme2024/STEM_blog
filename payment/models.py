from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Tariff(models.Model):
    name = models.CharField(max_length=250, verbose_name='Имя тарифа')
    price = models.FloatField(verbose_name='Стоимость')
    update_article = models.BooleanField(default=False, verbose_name ='Возможность обновлять статьи')
    delete_article = models.BooleanField(default=False, verbose_name ='Возможность удалить статьи')
    create_article = models.BooleanField(default=False, verbose_name ='Возможность создавать статьи')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'

class TemporarySave(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    tariff = models.ForeignKey(Tariff, on_delete=models.CASCADE)
