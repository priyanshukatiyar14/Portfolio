# Generated by Django 5.0.7 on 2024-07-20 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_skill_proficiency_skill_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='link',
            field=models.ImageField(blank=True, null=True, upload_to='skills/'),
        ),
    ]
