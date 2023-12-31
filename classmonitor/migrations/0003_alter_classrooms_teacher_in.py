# Generated by Django 5.0 on 2023-12-31 16:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classmonitor', '0002_alter_teachers_email_alter_teachers_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classrooms',
            name='teacher_in',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='current_teacher', to='classmonitor.teachers'),
        ),
    ]
