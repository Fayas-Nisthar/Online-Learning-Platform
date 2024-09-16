# Generated by Django 4.2.7 on 2024-07-27 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_course_difficulty_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certificate',
            name='course',
        ),
        migrations.RemoveField(
            model_name='certificatetemplate',
            name='name',
        ),
        migrations.AlterField(
            model_name='certificate',
            name='issued_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='certificatetemplate',
            name='course',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='template', to='core.course'),
        ),
    ]