# Generated by Django 2.1.4 on 2019-06-13 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_delete_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='subtitle',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]
