# Generated by Django 3.1.5 on 2021-03-06 19:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databasedesign', '0006_font_subsets'),
    ]

    operations = [
        migrations.AlterField(
            model_name='font',
            name='lastModified',
            field=models.DateField(default=datetime.date(2020, 1, 1)),
        ),
    ]
