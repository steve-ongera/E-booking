# Generated by Django 5.0.7 on 2024-08-08 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_person_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='date_of_issue',
            field=models.DateField(null=True),
        ),
    ]
