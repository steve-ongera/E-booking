# Generated by Django 5.0.7 on 2024-08-06 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='id_number',
            field=models.CharField(max_length=8),
        ),
    ]
