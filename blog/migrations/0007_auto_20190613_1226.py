# Generated by Django 2.1.4 on 2019-06-13 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='texrt',
            new_name='text',
        ),
    ]
