# Generated by Django 5.1.6 on 2025-02-23 14:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('poster_image', models.ImageField(blank=True, null=True, upload_to='programs/')),
                ('description', models.TextField()),
                ('more_description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MoreProgramPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='programs/more_photos/')),
                ('program', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='more_photos', to='nss.program')),
            ],
        ),
        migrations.CreateModel(
            name='ProgramPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='programs/photos/')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='nss.program')),
            ],
        ),
    ]
