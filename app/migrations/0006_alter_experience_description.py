# Generated by Django 5.0.7 on 2024-07-20 17:14

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_experience_location_alter_experience_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='description',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]