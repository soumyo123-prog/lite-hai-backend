# Generated by Django 2.2.6 on 2019-10-10 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0006_auto_20191010_0702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workshop',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
