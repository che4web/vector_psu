# Generated by Django 5.0.2 on 2024-02-14 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseapp', '0005_course_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='foo',
        ),
    ]