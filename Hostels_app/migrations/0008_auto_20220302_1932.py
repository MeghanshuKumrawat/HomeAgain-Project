# Generated by Django 3.0.5 on 2022-03-02 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hostels_app', '0007_auto_20220302_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostel_images',
            name='image',
            field=models.ImageField(upload_to='Hostel_images'),
        ),
    ]