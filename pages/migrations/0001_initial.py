# Generated by Django 5.1.3 on 2024-11-17 12:55

import django.core.validators
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
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Имя категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Имя тематики')),
            ],
            options={
                'verbose_name': 'Тематика',
                'verbose_name_plural': 'Тематику',
            },
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Заголовок')),
                ('quantity_views', models.IntegerField(default=0, verbose_name='Кло-во просмотров')),
                ('description', models.TextField(verbose_name='Описание')),
                ('card_description', models.TextField(validators=[django.core.validators.MinLengthValidator(25), django.core.validators.MaxLengthValidator(35)], verbose_name='Короткое описание')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовать')),
                ('is_banned', models.BooleanField(default=False, verbose_name='Заблокированная статья')),
                ('creation_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Время и дата создания')),
                ('updates_datetime', models.DateTimeField(auto_now=True, verbose_name='Время и дата обновления')),
                ('timing_article', models.TimeField(verbose_name='Хронометраж статьи')),
                ('slug', models.SlugField(max_length=250)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Автар статьи')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.categories', verbose_name='Категория')),
                ('subject_article', models.ManyToManyField(to='pages.subjects', verbose_name='Тематика статьи')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
        migrations.CreateModel(
            name='GalleryArticles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='articles/', verbose_name='Фотки')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_articles', to='pages.articles')),
            ],
        ),
    ]
