# Generated by Django 2.1.4 on 2019-06-24 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20190624_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(default=1, upload_to='photos'),
            preserve_default=False,
        ),
    ]
