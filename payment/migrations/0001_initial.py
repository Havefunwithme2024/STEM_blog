# Generated by Django 5.1.3 on 2024-12-06 12:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tariff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Имя тарифа')),
                ('price', models.FloatField(verbose_name='Стоимость')),
                ('delete_article', models.BooleanField(default=False, verbose_name='Возможность удалить статьи')),
            ],
            options={
                'verbose_name': 'Тариф',
                'verbose_name_plural': 'Тарифы',
            },
        ),
        migrations.CreateModel(
            name='TemporarySave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tariff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.tariff')),
            ],
        ),
    ]
