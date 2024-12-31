# Generated by Django 5.1.3 on 2024-12-01 13:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_commentauthenticated'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViewsArticles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_session', models.CharField(max_length=250)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.articles')),
            ],
        ),
    ]
