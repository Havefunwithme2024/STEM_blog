# Generated by Django 5.1.3 on 2024-11-24 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentAnonymous',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Автор комментария')),
                ('content', models.TextField(verbose_name='Описание комментария')),
                ('datetime_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
            ],
        ),
    ]
