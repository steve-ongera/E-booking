# Generated by Django 5.0.7 on 2024-08-06 10:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MarriageLicense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant1', models.CharField(max_length=100)),
                ('applicant2', models.CharField(max_length=100)),
                ('application_date', models.DateField(auto_now_add=True)),
                ('license_number', models.CharField(max_length=100, unique=True)),
                ('cert_pdf', models.FileField(blank=True, null=True, upload_to='media/cert_pdfs/')),
                ('issued_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyDeed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=100)),
                ('property_address', models.CharField(max_length=255)),
                ('deed_number', models.CharField(max_length=100, unique=True)),
                ('date_issued', models.DateField(auto_now_add=True)),
                ('deed_pdf', models.FileField(blank=True, null=True, upload_to='media/deed_pdfs/')),
                ('issued_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PublicRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_type', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date_created', models.DateField(auto_now_add=True)),
                ('id_image', models.ImageField(blank=True, null=True, upload_to='media/id_images/')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]