# Generated by Django 4.0 on 2022-02-04 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_kitobjanri_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kitobjanri',
            name='slug',
            field=models.SlugField(max_length=200),
        ),
    ]
