# Generated by Django 5.1 on 2024-11-27 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='date_joined',
            field=models.DateTimeField(default='2024-09-01', editable=False),
        ),
    ]
