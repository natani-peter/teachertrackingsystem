# Generated by Django 5.0 on 2023-12-30 17:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassRooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(choices=[('S1', 'S1'), ('S2', 'S2'), ('S3', 'S3'), ('S4', 'S4'), ('S5', 'S5'), ('S6', 'S6')], max_length=100)),
                ('stream', models.CharField(choices=[('S', 'S'), ('H', 'H')], max_length=5)),
                ('class_monitor', models.CharField(max_length=50)),
                ('state', models.BooleanField(db_default=models.Value(False))),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=50)),
                ('l_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('subjects', models.ManyToManyField(related_name='teacher_subjects', to='classmonitor.subjects')),
            ],
        ),
        migrations.CreateModel(
            name='Records',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('day', models.CharField(max_length=20)),
                ('week', models.CharField(max_length=20)),
                ('entry_time', models.TimeField(auto_now_add=True)),
                ('exit_time', models.TimeField(blank=True)),
                ('duration', models.TimeField(blank=True)),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='class_taught', to='classmonitor.classrooms')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject_taught', to='classmonitor.subjects')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Who_taught', to='classmonitor.teachers')),
            ],
        ),
        migrations.AddField(
            model_name='classrooms',
            name='class_teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='class_teacher', to='classmonitor.teachers'),
        ),
        migrations.AddField(
            model_name='classrooms',
            name='teacher_in',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='current_teacher', to='classmonitor.teachers'),
        ),
    ]
