# Generated by Django 5.1.7 on 2025-06-21 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowrecord',
            name='borrow_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='borrowrecord',
            name='return_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
