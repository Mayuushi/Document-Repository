# Generated by Django 5.1.3 on 2024-12-12 15:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_alter_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowrecord',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 17, 15, 16, 18, 701038, tzinfo=datetime.timezone.utc)),
        ),
    ]
