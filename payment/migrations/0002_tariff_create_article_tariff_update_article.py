# Generated by Django 5.1.3 on 2024-12-06 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tariff',
            name='create_article',
            field=models.BooleanField(default=False, verbose_name='Возможность создавать статьи'),
        ),
        migrations.AddField(
            model_name='tariff',
            name='update_article',
            field=models.BooleanField(default=False, verbose_name='Возможность обновлять статьи'),
        ),
    ]