# Generated by Django 5.0.7 on 2024-08-06 12:13

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_vehicle'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id_number', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField()),
                ('place_of_birth', models.CharField(max_length=255)),
                ('profile_picture', models.ImageField(upload_to='profile_pictures/')),
            ],
        ),
    ]
