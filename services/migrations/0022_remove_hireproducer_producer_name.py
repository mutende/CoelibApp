# Generated by Django 2.1.3 on 2019-03-24 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0021_auto_20190323_1640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hireproducer',
            name='producer_name',
        ),
    ]
