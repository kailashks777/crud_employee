# Generated by Django 3.2 on 2021-04-29 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_details', '0003_auto_20210429_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.BooleanField(max_length=6),
        ),
    ]
