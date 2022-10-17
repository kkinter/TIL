# Generated by Django 3.2.13 on 2022-10-17 07:55

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_article_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thumbnail',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='images/'),
        ),
    ]