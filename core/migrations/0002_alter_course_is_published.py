# Generated by Django 4.2.7 on 2024-07-26 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]
