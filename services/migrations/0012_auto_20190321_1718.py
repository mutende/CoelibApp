# Generated by Django 2.1.3 on 2019-03-21 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0011_remove_studiosessions_starting_time'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Hire_Producer',
            new_name='HireProducer',
        ),
    ]