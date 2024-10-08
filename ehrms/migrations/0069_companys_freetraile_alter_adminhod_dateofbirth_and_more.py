# Generated by Django 4.2.4 on 2023-12-29 03:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ehrms', '0068_alter_adminhod_dateofjoining_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='companys',
            name='freetraile',
            field=models.BooleanField(default=1),
        ),
        migrations.AlterField(
            model_name='adminhod',
            name='dateofbirth',
            field=models.DateField(default=datetime.date(2023, 12, 29)),
        ),
        migrations.AlterField(
            model_name='adminhod',
            name='dateofjoining',
            field=models.DateField(default=datetime.date(2023, 12, 29)),
        ),
        migrations.AlterField(
            model_name='employ_payslip',
            name='dateofbirth',
            field=models.DateField(default=datetime.date(2023, 12, 29)),
        ),
        migrations.AlterField(
            model_name='employeeloginlogout',
            name='login_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 29, 9, 26, 38, 398250)),
        ),
        migrations.AlterField(
            model_name='employs',
            name='dateofjoining',
            field=models.DateField(default=datetime.date(2023, 12, 29)),
        ),
        migrations.AlterField(
            model_name='hr',
            name='dateofbirth',
            field=models.DateField(default=datetime.date(2023, 12, 29)),
        ),
        migrations.AlterField(
            model_name='hr',
            name='dateofjoining',
            field=models.DateField(default=datetime.date(2023, 12, 29)),
        ),
        migrations.AlterField(
            model_name='projecttask',
            name='task_date',
            field=models.DateField(default=datetime.date(2023, 12, 29)),
        ),
        migrations.AlterField(
            model_name='tlassigntask',
            name='task_date',
            field=models.DateField(default=datetime.date(2023, 12, 29)),
        ),
        migrations.AlterField(
            model_name='working_shifts',
            name='ending_time',
            field=models.TimeField(default='17:00'),
        ),
        migrations.AlterField(
            model_name='working_shifts',
            name='starting_time',
            field=models.TimeField(default='08:00'),
        ),
    ]
