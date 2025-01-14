# Generated by Django 5.1 on 2024-12-26 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_profile_profile_picture_alter_profile_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_joined',
            field=models.DateTimeField(db_column='Data dołączenia', default='2024-09-01'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(db_column='Adres Email', default='twoj_email@gmail.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(db_column='Zdjęcie profilowe', default='pfps/blank_user.png', upload_to='pfps/'),
        ),
    ]
