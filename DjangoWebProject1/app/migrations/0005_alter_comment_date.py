# Generated by Django 4.2.13 on 2024-12-15 18:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_comment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2024, 12, 15, 21, 9, 17, 773243), verbose_name='Data comment'),
        ),
    ]