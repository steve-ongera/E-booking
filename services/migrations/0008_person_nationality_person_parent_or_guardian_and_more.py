# Generated by Django 5.0.7 on 2024-08-08 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_person_expiry_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='nationality',
            field=models.CharField(blank=True, default='Kenyan', max_length=50),
        ),
        migrations.AddField(
            model_name='person',
            name='parent_or_guardian',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='thumbprint',
            field=models.ImageField(null=True, upload_to='thumbprints/'),
        ),
    ]
