# Generated by Django 5.0.4 on 2024-05-06 17:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statsApp', '0002_buyurtma_tolandi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyurtma',
            name='raqam',
            field=models.AutoField(primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(1111)]),
        ),
    ]
