# Generated by Django 2.1.4 on 2019-06-09 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
    ]
