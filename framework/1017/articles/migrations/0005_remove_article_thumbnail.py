# Generated by Django 3.2.13 on 2022-10-17 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_article_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='thumbnail',
        ),
    ]
