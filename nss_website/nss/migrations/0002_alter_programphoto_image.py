# Generated by Django 5.1.6 on 2025-02-23 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nss', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programphoto',
            name='image',
            field=models.ImageField(upload_to='program_photos/'),
        ),
    ]
