# Generated by Django 5.0.7 on 2024-08-06 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(max_length=100)),
                ('owner_id_number', models.CharField(max_length=20)),
                ('number_plate', models.CharField(max_length=20, unique=True)),
                ('model', models.CharField(max_length=100)),
                ('year', models.PositiveIntegerField()),
                ('insured', models.BooleanField(default=False)),
                ('image1', models.ImageField(upload_to='vehicle_images/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='vehicle_images/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='vehicle_images/')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='vehicle_images/')),
                ('image5', models.ImageField(blank=True, null=True, upload_to='vehicle_images/')),
                ('image6', models.ImageField(blank=True, null=True, upload_to='vehicle_images/')),
            ],
        ),
    ]
