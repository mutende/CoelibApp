# Generated by Django 2.1.3 on 2019-03-23 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0020_auto_20190323_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hireproducer',
            name='hire_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='hireproducer',
            name='hire_time',
            field=models.TimeField(),
        ),
    ]