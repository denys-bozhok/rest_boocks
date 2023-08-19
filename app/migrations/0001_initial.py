# Generated by Django 4.2.3 on 2023-08-19 14:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=30, unique=True)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('description', models.TextField()),
                ('date', models.CharField(max_length=30)),
                ('slug', models.SlugField()),
            ],
        ),
    ]