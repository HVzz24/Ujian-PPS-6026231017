# Generated by Django 4.2.8 on 2023-12-14 17:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("questions", "0019_alter_exam_model_end_time_alter_exam_model_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="exam_model",
            name="end_time",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 12, 15, 0, 39, 15, 354579)
            ),
        ),
        migrations.AlterField(
            model_name="exam_model",
            name="start_time",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 12, 15, 0, 39, 15, 354579)
            ),
        ),
    ]
