# Generated by Django 2.1.4 on 2019-06-09 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default=0, upload_to='photos'),
            preserve_default=False,
        ),
    ]