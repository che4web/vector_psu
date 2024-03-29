# Generated by Django 5.0.2 on 2024-03-16 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courseapp', '0007_course_study_load'),
        ('programapp', '0005_ege_programege'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('course', models.ManyToManyField(blank=True, to='courseapp.course')),
                ('speciality', models.ManyToManyField(blank=True, to='programapp.speciality')),
            ],
        ),
    ]
