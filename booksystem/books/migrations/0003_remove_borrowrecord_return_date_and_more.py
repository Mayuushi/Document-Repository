# Generated by Django 5.1.1 on 2024-10-24 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_available_borrowrecord'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrowrecord',
            name='return_date',
        ),
        migrations.AddField(
            model_name='borrowrecord',
            name='returned',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='borrowrecord',
            name='borrower_name',
            field=models.CharField(max_length=100),
        ),
    ]
