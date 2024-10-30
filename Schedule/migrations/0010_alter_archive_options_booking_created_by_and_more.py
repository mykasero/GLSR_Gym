# Generated by Django 5.1 on 2024-10-30 21:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Schedule', '0009_alter_archive_users_amount'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='archive',
            options={'ordering': ['-current_day']},
        ),
        migrations.AddField(
            model_name='booking',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start_hour',
            field=models.TimeField(db_column='Start', help_text='Podaj godzine w formacie np.: 12:20, lub zacznij podawać numery i wybierz odpowiadający ci z listy domyślnych wyborów (na tel nad klawiaturą)'),
        ),
    ]
