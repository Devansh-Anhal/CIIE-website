# Generated by Django 2.1.7 on 2019-04-10 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0003_title_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='url',
            field=models.CharField(default='#', max_length=255),
        ),
    ]