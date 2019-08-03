# Generated by Django 2.1.7 on 2019-03-07 18:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('FirstName', models.CharField(max_length=300, validators=[django.core.validators.RegexValidator(code='invalid_name', message='Name should contain only alphabets', regex='^[a-zA-Z]+$')])),
                ('LastName', models.CharField(max_length=300, validators=[django.core.validators.RegexValidator(code='invalid_name', message='Name should contain only alphabets', regex='^[a-zA-Z]+$')])),
                ('University', models.CharField(max_length=300, validators=[django.core.validators.RegexValidator(code='invalid_name', message='University name should contain only alphabets', regex='^[a-zA-Z]+$')])),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
