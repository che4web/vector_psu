# Generated by Django 5.0.1 on 2024-02-07 07:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseapp', '0003_course_prof_typ'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=222)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='foo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courseapp.foo'),
        ),
    ]
