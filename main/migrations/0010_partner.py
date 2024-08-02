# Generated by Django 5.0.7 on 2024-08-01 18:27

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_remove_profile_first_name_remove_profile_last_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('description', models.TextField(max_length=2000)),
                ('img', models.ImageField(upload_to='events_imgs/', verbose_name='100x100')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]