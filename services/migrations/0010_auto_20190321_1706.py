# Generated by Django 2.1.3 on 2019-03-21 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0009_auto_20190320_1912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hire_producer',
            name='available_date',
        ),
        migrations.RemoveField(
            model_name='hire_producer',
            name='duration_hrs',
        ),
    ]