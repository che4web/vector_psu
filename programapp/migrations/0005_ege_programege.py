# Generated by Django 5.0.2 on 2024-03-02 05:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programapp', '0004_program_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ege',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ProgramEge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('ege', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='programapp.ege')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programapp.program')),
            ],
        ),
    ]