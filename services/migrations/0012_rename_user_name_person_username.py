# Generated by Django 5.0.7 on 2024-08-11 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0011_person_user_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='user_name',
            new_name='username',
        ),
    ]
