# Generated by Django 5.1.1 on 2024-10-24 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_remove_borrowrecord_return_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrowrecord',
            name='returned',
        ),
        migrations.AddField(
            model_name='borrowrecord',
            name='return_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='borrowrecord',
            name='borrower_name',
            field=models.CharField(max_length=200),
        ),
    ]