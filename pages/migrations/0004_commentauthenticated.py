# Generated by Django 5.1.3 on 2024-12-01 13:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_commentanonymous_article'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentAuthenticated',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Описание комментария')),
                ('creation_time', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.articles', verbose_name='Статья')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор комментария')),
            ],
        ),
    ]