# Generated by Django 4.2.13 on 2024-06-06 14:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2024, 6, 6, 17, 12, 4, 505228), verbose_name='Data comment'),
        ),
    ]