# Generated by Django 5.0.2 on 2024-03-30 03:58

import django.db.models.deletion
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseapp', '0009_alter_course_img'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalCourse',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название курса')),
                ('study_load', models.IntegerField(blank=True, default=0)),
                ('known_area', models.CharField(blank=True, choices=[('FZ', 'Физика'), ('MT', 'Математика'), ('IT', 'Информационные технологии')], default='FZ', max_length=2)),
                ('prof_typ', models.CharField(blank=True, choices=[('B', 'Базова'), ('P', 'Профизионнальная'), ('V', 'По выбору')], default='B', max_length=1)),
                ('date', models.DateField(blank=True, null=True)),
                ('img', models.TextField(blank=True, max_length=100, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical course',
                'verbose_name_plural': 'historical courses',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
