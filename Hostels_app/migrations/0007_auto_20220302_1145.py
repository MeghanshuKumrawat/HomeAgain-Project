# Generated by Django 3.0.5 on 2022-03-02 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hostels_app', '0006_auto_20220301_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostel',
            name='lat',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hostel',
            name='log',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hostel',
            name='one_seater_price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='hostel',
            name='one_seater_room',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='hostel',
            name='three_seater_price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='hostel',
            name='three_seater_room',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='hostel',
            name='two_seater_price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='hostel',
            name='two_seater_room',
            field=models.IntegerField(null=True),
        ),
    ]
