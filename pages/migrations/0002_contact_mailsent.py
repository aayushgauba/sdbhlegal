# Generated by Django 5.1 on 2024-09-07 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='mailSent',
            field=models.BooleanField(default=False),
        ),
    ]
