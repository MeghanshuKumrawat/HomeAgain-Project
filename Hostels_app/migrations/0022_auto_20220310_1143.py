# Generated by Django 3.0.5 on 2022-03-10 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hostels_app', '0021_auto_20220309_1200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hostel',
            name='log',
        ),
        migrations.AddField(
            model_name='hostel',
            name='boys',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='hostel',
            name='girls',
            field=models.FloatField(null=True),
        ),
    ]