# Generated by Django 3.2.5 on 2021-08-04 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todowoo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='datecompleted',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
