# Generated by Django 4.0 on 2022-01-18 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kitobjanri',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Janrnomi')),
            ],
            options={
                'verbose_name': 'Janr',
                'verbose_name_plural': 'Janrlar',
            },
        ),
    ]
