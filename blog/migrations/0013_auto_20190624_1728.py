# Generated by Django 2.1.4 on 2019-06-24 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20190624_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='photo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Photo'),
        ),
        migrations.AddField(
            model_name='photo',
            name='name',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]
