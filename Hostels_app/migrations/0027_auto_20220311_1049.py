# Generated by Django 3.0.5 on 2022-03-11 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hostels_app', '0026_auto_20220310_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostel',
            name='category',
            field=models.CharField(choices=[('boys', 'Boys'), ('girls', 'Girls'), ('C', 'CoEd')], max_length=5),
        ),
    ]
