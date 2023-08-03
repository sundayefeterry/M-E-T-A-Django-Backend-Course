# Generated by Django 4.2.1 on 2023-07-14 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_logger'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='person_name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='phone',
        ),
        migrations.AddField(
            model_name='person',
            name='first_name',
            field=models.CharField(default='first_name', max_length=200),
        ),
        migrations.AddField(
            model_name='person',
            name='last_name',
            field=models.CharField(default='last_name', max_length=200),
        ),
    ]