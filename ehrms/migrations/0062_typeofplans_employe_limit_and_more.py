# Generated by Django 4.2.4 on 2023-12-22 13:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ehrms', '0061_featurestypes_show1_featurestypes_show2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='typeofplans',
            name='employe_limit',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='employeeloginlogout',
            name='login_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 22, 18, 50, 22, 195942)),
        ),
    ]
