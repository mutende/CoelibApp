# Generated by Django 2.1.3 on 2019-03-19 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20190319_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hire_producer',
            name='available_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]